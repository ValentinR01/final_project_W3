locals {
  resource_groups = {
    "prod"   =  var.prod
    "preprod" = var.preprod
  }
}


resource "azurerm_resource_group" "resource_group" {
  for_each = local.resource_groups
  name     = each.value
  location = var.location

  tags = {
    environment = each.key
  }
}


resource "azurerm_virtual_machine" "vm" {
  for_each            = azurerm_resource_group.resource_group
  name                = "${each.value.name}-vm"
  resource_group_name = each.value.name
  location            = each.value.location
  network_interface_ids = [azurerm_network_interface.network_interface[each.key].id]
  vm_size               = "Standard_B1ls"

  delete_os_disk_on_termination = true
  delete_data_disks_on_termination = true

  storage_image_reference {
    offer  = "0001-com-ubuntu-server-focal"
    publisher = "Canonical"
    sku    = "20_04-lts-gen2"
    version   = "latest"
  }

  storage_os_disk {
    name              = "osdisk1"
    caching           = "ReadWrite"
    create_option     = "FromImage"
    managed_disk_type = "Standard_LRS"
  }

  os_profile {
    computer_name  = each.value.name
    admin_username = var.cd_username
  }

  os_profile_linux_config {
    disable_password_authentication = true

    ssh_keys {
      path     = "/home/${var.cd_username}/.ssh/authorized_keys"
      key_data = ""

    }
  }

  tags = {
    environment = each.key
  }
}


resource "azurerm_virtual_machine_extension" "example" {
  for_each             = azurerm_resource_group.resource_group
  name                 = "${each.value.name}-vm-extension"
  virtual_machine_id   = azurerm_virtual_machine.vm[each.key].id
  publisher            = "Microsoft.Azure.Extensions"
  type                 = "CustomScript"
  type_handler_version = "2.0"

  protected_settings = <<PROTECTED_SETTINGS
    {
      "script": "${base64encode(templatefile("scripts/init.sh", {
        cd_username = var.cd_username
      }))}"
    }
  PROTECTED_SETTINGS
}


resource "azurerm_container_registry" "acr" {
  for_each            = azurerm_resource_group.resource_group
  name                = "saline${each.key}"
  resource_group_name = each.value.name
  location            = each.value.location
  sku                 = "Basic"
  admin_enabled       = true
}