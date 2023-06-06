output "prod-saline-ip_address" {
  value       = digitalocean_droplet.prod-saline.ipv4_address
  description = "Saline production IP address"
}

output "preprod-saline-ip_address" {
  value       = digitalocean_droplet.preprod-saline.ipv4_address
  description = "Saline pre-production IP address"
}