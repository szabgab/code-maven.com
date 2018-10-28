import gntp.notifier
growl = gntp.notifier.GrowlNotifier(
    applicationName = "My Application Name",
    notifications = ["New Updates","New Messages"],
    defaultNotifications = ["New Messages"],
)
growl.register()

growl.notify(
    noteType = "New Messages",
    title = "You have a new message",
    description = "A longer message description",
    sticky = False,
    priority = 1,
)

