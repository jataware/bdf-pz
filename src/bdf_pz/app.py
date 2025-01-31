import json
import os

from beaker_kernel.lib.app import BeakerApp, BeakerAppAsset, AppConfigStrings, Context


class PalimpzestApp(BeakerApp):
    SLUG = "palimpzest"
    ASSET_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "assets"))

    pages = {
        'chat': {
            "title": "Palimpzest chat",
            "default": True,
        },
        "notebook": {
            "title": "Palimpzest notebook",
        }
    }
    default_context = Context(
        slug="bdf-pz",
        payload={},
    )
    single_context = True

    assets = [
        BeakerAppAsset(
            slug="header_logo",
            src="palimpzest-cropped.png",
            alt="Palimpzest logo"
        ),
        BeakerAppAsset(
            slug="body_logo",
            src="palimpzest-cropped.png",
            alt="Palimpzest cropped logo"
        )
    ]
    strings = AppConfigStrings(
        short_title="Palimpzest",
        chat_welcome_html="""<div style="display: flex; flex-direction: row; align-items: center; gap: 20px;">
          <img src="/assets/palimpzest/palimpzest-cropped.png" alt="Palimpzest Logo" height="75px">
          <p>Hi! I'm your Palimpzest Agent and I can help you do all sorts of information extraction tasks. Your first step is to upload
          some documents or datasets to get started. Then let me know what kind of information you'd like to extract from them.
          Let me know what you'd like to do so I can best assist you!</p>
        </div>"""
    )
