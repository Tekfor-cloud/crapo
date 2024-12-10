# pylint: disable=missing-docstring
{
    "name": "Crapo: Automaton",
    "version": "16.0.3.0.0",
    "category": "Crapo Automata & Workflows",
    "author": "Article714",
    "license": "LGPL-3",
    "website": "https://www.article714.org",
    "summary": """ Create and manage automata on models """,
    "depends": ["queue_job", "crapo_base"],
    "data": [
        "security/automaton_action.xml",
        "security/crapo_automaton_mixin.xml",
        "security/automaton.xml",
        "security/automaton_transition.xml",
        "security/automaton_condition.xml",
        "security/automaton_state.xml",
        "data/job.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "crapo_automaton/static/src/js/statusbar_field.js"
        ],
    },
    "installable": True,
    "images": [],
    "application": True,
}
