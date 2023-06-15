*** Settings ***
Library    SeleniumLibrary

*** Variables ***

#${OUTPUT_DIR}            d:\scripts\robot_framework_playground\Results\

*** Test Cases ***
Launch Browser
    open browser    https://www.google.com/     chrome
    log to console    ${OUTPUT_DIR}

*** Keywords ***
