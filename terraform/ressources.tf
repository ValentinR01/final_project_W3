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
    admin_username = var.admin_username
    admin_password = var.admin_password
  }

  os_profile_linux_config {
    disable_password_authentication = false
  }

  tags = {
    environment = each.key
  }
}

resource "azurerm_container_registry" "acr" {
  for_each            = azurerm_resource_group.resource_group
  name                = "saline${each.key}"
  resource_group_name = each.value.name
  location            = each.value.location
  sku                 = "Basic"
  admin_enabled       = true
}
