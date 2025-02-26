
from beaker_kernel.lib.app import BeakerApp


class PalimpzestApp(BeakerApp):
    slug = "palimpzest"
    name = "PalimpChat"

    pages = {
        "chat": {
            "title": "{app_name}",
            "default": True,
        },
        "notebook": {
            "title": "Palimpzest notebook",
        },
        "dev": {
            "title": "Palimpzest dev interface",
        }
    }

    stylesheet = "global_stylesheet"

    default_context = {
        "slug": "bdf-pz",
        "payload": {},
        "single_context": True,
    }

    assets = {
        "header_logo": {
            "src": "palimpzest-cropped.png",
            "alt": "{app_name} logo",
        },
        "body_logo": {
            "src": "palimpzest-cropped.png",
            "alt": "{app_name} cropped logo",
            "height": "75px"
        },
        "global_stylesheet": {
            "src": "style.css",
        }
    }

    template_bundle = {
        "short_title": "{app_name}",
        "chat_welcome_html": """<div style="display: flex; flex-direction: row; align-items: center; gap: 20px;">
          <img src="{asset:body_logo:src}" alt="{asset:body_logo:alt}" height="{asset:body_logo:height}">
          <p>Hi! I'm your Palimpzest Agent and I can help you do all sorts of information extraction tasks. Your first step is to upload
          some documents or datasets to get started. Then let me know what kind of information you'd like to extract from them.
          Let me know what you'd like to do so I can best assist you!</p>
        </div>""",
    }
