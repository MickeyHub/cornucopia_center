# Cornucopia Center

This is the plugin center for [cornucopia](https://github.com/MickeyHub/cornucopia) app. This repo is also open to all of you. feel free to share your plugins and happiness. Here, I'll detail the requirements and workflow of making and publish plugins.

## Make Your Plugin

*Plugin is a dynamic framework built in Xcode*

It's easy to build a plugin, just create a framework target in any project. create an UIViewController as the entrance of plugin. add a Cornucopia.plist. check the sample plugin to get a concrete understand: [qrcode_generator](https://github.com/MickeyHub/cornucopia_qrcode_generator).

Despite of the fact that the framework contains many files. The plugin only consist of the `executable file` and the `Cornucopia.plist`.

Since all of plugins are running on the same sandbox and process. so we have to follow some rules to make it healthy when growing up.

#### UI Design

* Don't use other icon resources as much as possible, SF Symbol is great option.
* Don't customize system UI element as much as possible, keep the style consistent with other plugin and the Host app.

#### Disk

* Disk storage in sandbox should be in the respective folder named with plugin name. For example, when we are saving data to the Documents or Library/Cache or others, we should create a directory at first named with your plugin name like `/Documents/qrcode_generator/xxx.db`.
* UserDefaults should be used with `init(suiteName:)` to build an individual plist file in Preferences folder.
* When user delete the plugin, all of those folders will be checked and deleted automatically.

#### Memory

* Don't use custom global object as much as possible. like singleton or something
* Don't leak memory out of your plugin. When user leave your plugin, all of the memory allocated in the plugin should be released.

#### Language

* Prefer using Swift, because it supports namespace which avoids the conflict over symbols
* Keep in mind that use the full class name in the entry field in Cornucopia.plist if you write the plugin in Swift. like `qrcode_generator.EntryController`.

#### Privacy

* For privacy you wanna enable, you can contract me and discuss the reason, I'll add it for you and publish the iteration asap.

## Submit Your Plugin

When you finish writing your own plugin, all you need to do is creating an issue attached with your plugin repo. I'll review and test it according the rules mentioned above. If passed, I'll build by myself and publish it to the center.

## Submit Your Idea

Also, you can just create an issue with only idea. If it's useful and feasible, I'll be glad to create the plugin for you.
