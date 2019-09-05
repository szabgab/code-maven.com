provider "google" {
  project     = "project-name-1234"
  region      = "us-central1"
}

resource "google_compute_instance" "gabor" {
  name         = "gabor-1"
  machine_type = "f1-micro"
  zone         = "us-central1-a"

  boot_disk {
    initialize_params {
      image = "ubuntu-1804-lts"
    }
  }

  network_interface {
    subnetwork = "central1-resources"
  }
}



