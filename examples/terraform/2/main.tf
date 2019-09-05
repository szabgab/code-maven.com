provider "google" {
  project     = "project-name-12345"
  region      = "us-central1"
}

resource "google_compute_instance" "gabor" {
  name         = "gabor-${count.index + 1}"
  machine_type = "f1-micro"
  zone         = "us-central1-b"
  count        = "2"

  labels = {
    owner = "gabor"
    group = "devops"
  }

#  tags = ["access-external"]

  boot_disk {
    initialize_params {
      image = "ubuntu-1804-lts"
    }
  }

  network_interface {
    subnetwork = "central1-resources"
  }

  scheduling {
    preemptible  = false
    automatic_restart = false
  }
}


