# Dublit & Dragons

Welcome to Dublit & Dragons – your innovative assistant geared towards enhancing the Dungeons & Dragons (D&D) experience for Game Masters (GMs). This powerful tool utilizes AI to craft various elements for D&D campaigns, such as character tokens, encounter maps, backstories, stat blocks, and more. This assistant intends to stay within established D&D lore and rules; however, as a new and general purpose LLM (ModelFarm by Rplit) it will go outside of the lore and rules on occasion. By using services such as the dnd5eAPI, we are able to create a RAG-like functionality to keep the assistant within context in certain scenarios.

## Features

- **Character Generation**: Craft detailed character tokens with associated stat blocks and narratives.
- **Encounter Generation**: Generate encounters complete with maps and descriptions fitting your game's theme.
- **Area Generation**: Design comprehensive area maps and descriptions to enrich your D&D world.
- **Item Generation**: Create custom items with unique stat blocks for your campaign.

## Usage

Access the assistant via the web interface and utilize the radio buttons to select the type of content you wish to generate. Input your prompt in the text field and click the generate button to receive custom-tailored content through AI generation.

## DnD5e API Integration

The DnD5e API provides a robust foundation for the assistant by offering a reference to well-established game elements. Current integration is minimal but enriches AI prompts with accurate D&D data, providing a "Rule-As-Given" (RAG) experience.

### Current Implementation

The integration currently includes fetching monster lists from the D&D universe to validate encounter authenticity against the official rule set, using the 347 freely available D&D monsters.

### Future Plans

We aim to broaden API usage with detailed class, race, spell, and equipment data which will serve to further refine the AI's prompts and adherence to official lore and mechanics. *"Homebrewing"* with the help of AI is also a core feature of this assistant and while being lore-accurate can make things easy, there is just as much value in building out the features that streamline creation processes for homebrewed items, classes, races, spells, and settings.

## Get Started

Fork the repo and add your OpenAI API key to the secrets and you are good to go! 🥳🎉