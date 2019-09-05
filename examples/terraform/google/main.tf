#variable "region" { default = "us-central1" }
variable "name" { }
variable "zone" { default = "us-central1-a" }

provider "google" {
 project     = "project-name-12345"
#  region      = "${var.region}"
}

resource "google_compute_instance" "gabor" {
 name         = var.name
 machine_type = "f1-micro"
 zone         = "${var.zone}"

 boot_disk {
   initialize_params {
     image = "ubuntu-1804-lts"
   }
 }

 network_interface {
   subnetwork = "gce-d-us-central1-indexing"
 }

 labels = {
   activity    = "temp"
   delete_at   = "never"
   group       = "devops"
   owner       = "gabor"
   start_at    = "never"
   stop_at     = "never"
 }

 connection {
     type     = "ssh"
     user     = "gabor"
     host     = var.name
 }

 provisioner "file" {
   source = "startup.sh"
   destination = "/home/gabor/startup.sh"
 }

 provisioner "remote-exec" {
   inline = [
      "chmod +x /home/gabor/startup.sh"
      #"apt-get update",
      #"apt-get install -y htop",
   ]
 }

 metadata = {
   "startup-script" : "/home/gabor/startup.sh"
 }
 #metadata_startup_script = "date >> /opt/test.txt"
}

