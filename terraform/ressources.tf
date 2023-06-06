resource "digitalocean_droplet" "prod-saline" {
    image = "ubuntu-22-10-x64"
    size = "s-1vcpu-1gb"
    region =  var.region
    name = "prod-saline"
}

resource "digitalocean_droplet" "preprod-saline" {
    image = "ubuntu-22-10-x64"
    size = "s-1vcpu-1gb"
    region =  var.region
    name = "prod-saline"    
}