# Notice of discontinuation
This project has been unmaintained for a long time and no updates are planned for it. If you have stumbled across this in your search, please know there are much better libraries that implement features better and are still actively maintained. Thanks for your interest.

# neopixel-utilities

---
## Table of contents
- [Intro](#intro)
- [Features](#features)
- [Installation](#installation)
    - [Configuration](#configuration)
- [Documentation](#documenation)
- [Credits](#credits)
- [Licensing](#licensing)
---

## Intro

Neopixel-utilities is a Python wrapper I wrote for adding functionality to LED boards to be easier. It's not very well documented at the moment, and support for it is very limited. If this gains any traction, support and documentation may become better in the future. 

## Features

neopixel-utilities comes with several tools already that make development with LED boards significantly easier. This wrapper is capable of:

- Displaying stationary and scrolling text with early cutoff points
- Coordinate system so you can treat the LED board as a grid, instead of using Neopixel's pixel array system
- Switchboard functionality, with the ability to activate multiple pixels with different colors in one function
- Image converter
- Animation player with looping, FPS, and other features
- Font system with ability to add your own

along with other features!

## Installation

`pip install neopixel-utilities`

### Configuration

Configuration can be done by adding additional parameters to the `init` function.
Any additional arguments that are passed through this function will be passed on to the Neopixel library.

## Documentation

[Visit the wiki for instructions to get started and the docs!](https://github.com/Mahlarian/neopixel-utilities/wiki)

## Credits

Thank you to these people for their contributions to this project!
- The creators of Neopixel for creating Neopixel in the first place
- [Bytewave](https://github.com/BytewaveMLP) For hours of his help with general questions I had
- [Brittank88](https://github.com/Brittank88) For ideas and motivation
- [Randoragon](https://github.com/Randoragon) For ideas and motivation
- EvilFlame For help with formula for resolution scaling

## Licensing

Copyright (c) Mahlarian, 2021. This project is protected and licensed under the [GNU General Public License v3.0](/LICENSE)
