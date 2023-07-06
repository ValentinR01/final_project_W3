resource "azurerm_virtual_network" "virtual_network" {
  for_each            = azurerm_resource_group.resource_group
  name                = "${each.value.name}-virtual-network"
  address_space       = ["10.0.0.0/16"]
  location            = each.value.location
  resource_group_name = each.value.name

  tags = {
    environment = each.key
  }
}

resource "azurerm_subnet" "subnet" {
  for_each            = azurerm_resource_group.resource_group
  name                 = "${each.value.name}-subnet"
  resource_group_name  = each.value.name
  virtual_network_name = azurerm_virtual_network.virtual_network[each.key].name
  address_prefixes     = ["10.0.1.0/24"]
}

resource "azurerm_public_ip" "public_ip" {
  for_each            = azurerm_resource_group.resource_group
  name                = "${each.value.name}-publicip"
  location            = each.value.location
  resource_group_name = each.value.name
  allocation_method   = "Static"
  sku                 = "Standard"
}

resource "azurerm_network_interface" "network_interface" {
  for_each            = azurerm_resource_group.resource_group
  name                      = "${each.value.name}-network_interface"
  location                  = each.value.location
  resource_group_name       = each.value.name
  ip_configuration {
    name                          = "${each.value.name}-ipconfig"
    private_ip_address_allocation = "Dynamic"
    subnet_id = azurerm_subnet.subnet[each.key].id
    public_ip_address_id          = azurerm_public_ip.public_ip[each.key].id
  }
}

resource "azurerm_network_security_group" "security_group" {
    for_each            = azurerm_resource_group.resource_group
    name                = "${each.value.name}-security-group"
    location            = each.value.location
    resource_group_name = each.value.name

    security_rule {
        name                       = "SSH"
        priority                   = 1001
        direction                  = "Inbound"
        access                     = "Allow"
        protocol                   = "Tcp"
        source_port_range          = "*"
        destination_port_range     = "22"
        source_address_prefix      = "*"
        destination_address_prefix = "*"
    }

    security_rule {
          name                       = "HTTP"
          priority                   = 1002
          direction                  = "Outbound"
          access                     = "Allow"
          protocol                   = "Tcp"
          source_port_range          = "*"
          destination_port_range     = "80"
          source_address_prefix      = "*"
          destination_address_prefix = "*"
      }

    tags = {
        environment = each.key
    }
}

resource "azurerm_subnet_network_security_group_association" "mgmt-nsg-association" {
    for_each                  = azurerm_resource_group.resource_group
    subnet_id                 = azurerm_subnet.subnet[each.key].id
    network_security_group_id = azurerm_network_security_group.security_group[each.key].id
}