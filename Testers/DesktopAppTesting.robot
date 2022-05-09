*** Settings ***
# Documentation     Simple example using SeleniumLibrary.
Documentation     Simple example using AutoItLibrary.
Library           SeleniumLibrary
Library           AutoItLibrary


*** Variables ***
# ${WEBSITE URL}      https://www.amazon.com/
# ${BROWSER}          Chrome

*** Test Cases ***
# Open Test Website And Close Browser
Automate GUI
    Log to console  Hello Robot
    # Wina
    # Run     notepad.exe
    Tuz
    
    # Win minimize all
    # Win Minimize All
    # Win Minimize All
    # Get Auto It Version
# method  WinMinimizeAll
    # Open Test Website In Chrome
    # [Teardown]    Close Browser

*** Keywords ***
# Get Auto It Version
Tuz
    Run     notepad.exe
# Wina
#     Win Get Pos X   strTitle=Untitled - Notepad, strText=Hi

#     Win Minimize All

# Open Test Website In Chrome
    # Open Browser      ${WEBSITE URL}    ${BROWSER}
#     Sleep             2
#     Title Should Be   Amazon.com. Spend less. Smile more.
    # Control Get Pos X
    # Win Minimize All

