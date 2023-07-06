output "public_ip_addresses" {
  description = "Public IP addresses of the resource groups"
  value = {
    for rg in azurerm_resource_group.resource_group :
    rg.name => azurerm_public_ip.public_ip[rg.tags.environment].ip_address
  }
}