---
title: VirtualBox
timestamp: 2025-11-09T08:30:01
tags:
  - virtualbox
published: true
author: szabgab
archive: true
---

VirtualBox did not allow the Windows Machine to run:

I asked Chat GPT:

I have a Linux machine running ubuntu 2025.04. On it I have VirtualBox installed. I used to be able to run an MS Windows guest in it but not any more. It gives me the following error AMD-V is being used by another hypervisor (VERR_SVM_IN_USE). VirtualBox can't enable the AMD-V extension. Please disable the KVM kernel extension, recompile your kernel and reboot (VERR_SVM_IN_USE How can I fix this?

```
sudo systemctl stop libvirtd     # this gave an error
sudo modprobe -r kvm_amd kvm     # this helped me
```


