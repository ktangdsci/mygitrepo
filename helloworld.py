[
  {
    "op": "core/text-transform",
    "description": "Text transform on cells in column interview_date using expression value.toDate()",
    "engineConfig": {
      "facets": [],
      "mode": "row-based"
    },
    "columnName": "interview_date",
    "expression": "value.toDate()",
    "onError": "keep-original",
    "repeat": false,
    "repeatCount": 10
  },
  {
    "op": "core/mass-edit",
    "description": "Mass edit cells in column village",
    "engineConfig": {
      "facets": [],
      "mode": "row-based"
    },
    "columnName": "village",
    "expression": "value",
    "edits": [
      {
        "fromBlank": false,
        "fromError": false,
        "from": [
          "Ruaca-Nhamuenda",
          "Ruaca - Nhamuenda"
        ],
        "to": "Ruaca-Nhamuenda"
      }
    ]
  },
  {
    "op": "core/text-transform",
    "description": "Text transform on cells in column liv_owned using expression grel:value.replace('[', '').replace(']', '')",
    "engineConfig": {
      "facets": [],
      "mode": "row-based"
    },
    "columnName": "liv_owned",
    "expression": "grel:value.replace('[', '').replace(']', '')",
    "onError": "keep-original",
    "repeat": false,
    "repeatCount": 10
  },
  {
    "op": "core/text-transform",
    "description": "Text transform on cells in column liv_owned using expression grel:value.replace('\\'', '')",
    "engineConfig": {
      "facets": [],
      "mode": "row-based"
    },
    "columnName": "liv_owned",
    "expression": "grel:value.replace('\\'', '')",
    "onError": "keep-original",
    "repeat": false,
    "repeatCount": 10
  },
  {
    "op": "core/text-transform",
    "description": "Text transform on cells in column liv_owned using expression grel:value.replace(';', '\\t')",
    "engineConfig": {
      "facets": [],
      "mode": "row-based"
    },
    "columnName": "liv_owned",
    "expression": "grel:value.replace(';', '\\t')",
    "onError": "keep-original",
    "repeat": false,
    "repeatCount": 10
  },
  {
    "op": "core/text-transform",
    "description": "Text transform on cells in column items_owned using expression grel:value.replace('[', '').replace(']', '')",
    "engineConfig": {
      "facets": [],
      "mode": "row-based"
    },
    "columnName": "items_owned",
    "expression": "grel:value.replace('[', '').replace(']', '')",
    "onError": "keep-original",
    "repeat": false,
    "repeatCount": 10
  },
  {
    "op": "core/text-transform",
    "description": "Text transform on cells in column items_owned using expression grel:value.replace('\\'', '').replace(';','\\n')",
    "engineConfig": {
      "facets": [],
      "mode": "row-based"
    },
    "columnName": "items_owned",
    "expression": "grel:value.replace('\\'', '').replace(';','\\n')",
    "onError": "keep-original",
    "repeat": false,
    "repeatCount": 10
  },
  {
    "op": "core/mass-edit",
    "description": "Mass edit cells in column village",
    "engineConfig": {
      "facets": [],
      "mode": "row-based"
    },
    "columnName": "village",
    "expression": "value",
    "edits": [
      {
        "fromBlank": false,
        "fromError": false,
        "from": [
          "Villiage_B"
        ],
        "to": "Village_B"
      }
    ]
  },
  {
    "op": "core/mass-edit",
    "description": "Mass edit cells in column village",
    "engineConfig": {
      "facets": [],
      "mode": "row-based"
    },
    "columnName": "village",
    "expression": "value",
    "edits": [
      {
        "fromBlank": false,
        "fromError": false,
        "from": [
          "Villiage_C"
        ],
        "to": "Village_C"
      }
    ]
  },
  {
    "op": "core/mass-edit",
    "description": "Mass edit cells in column village",
    "engineConfig": {
      "facets": [],
      "mode": "row-based"
    },
    "columnName": "village",
    "expression": "value",
    "edits": [
      {
        "fromBlank": false,
        "fromError": false,
        "from": [
          "49"
        ],
        "to": "Village_C"
      }
    ]
  },
  {
    "op": "core/mass-edit",
    "description": "Mass edit cells in column village",
    "engineConfig": {
      "facets": [],
      "mode": "row-based"
    },
    "columnName": "village",
    "expression": "value",
    "edits": [
      {
        "fromBlank": false,
        "fromError": false,
        "from": [
          "Ruaca-Nhamuenda"
        ],
        "to": "Village_B"
      }
    ]
  },
  {
    "op": "core/text-transform",
    "description": "Text transform on cells in column months_no_water using expression grel:value.replace('[', '').replace(']', '').replace('\\'', '').replace(';', '\\n')",
    "engineConfig": {
      "facets": [],
      "mode": "row-based"
    },
    "columnName": "months_no_water",
    "expression": "grel:value.replace('[', '').replace(']', '').replace('\\'', '').replace(';', '\\n')",
    "onError": "keep-original",
    "repeat": false,
    "repeatCount": 10
  },
  {
    "op": "core/text-transform",
    "description": "Text transform on cells in column months_lack_food using expression grel:value.replace('[', '').replace(']', '').replace('\\'', '').replace(';', '\\n')",
    "engineConfig": {
      "facets": [],
      "mode": "row-based"
    },
    "columnName": "months_lack_food",
    "expression": "grel:value.replace('[', '').replace(']', '').replace('\\'', '').replace(';', '\\n')",
    "onError": "keep-original",
    "repeat": false,
    "repeatCount": 10
  },
  {
    "op": "core/text-transform",
    "description": "Text transform on cells in column no_food_mitigation using expression grel:value.replace('[', '').replace(']', '').replace('\\'', '').replace(';', '\\n')",
    "engineConfig": {
      "facets": [],
      "mode": "row-based"
    },
    "columnName": "no_food_mitigation",
    "expression": "grel:value.replace('[', '').replace(']', '').replace('\\'', '').replace(';', '\\n')",
    "onError": "keep-original",
    "repeat": false,
    "repeatCount": 10
  },
  {
    "op": "core/text-transform",
    "description": "Text transform on cells in column years_farm using expression value.toNumber()",
    "engineConfig": {
      "facets": [],
      "mode": "row-based"
    },
    "columnName": "years_farm",
    "expression": "value.toNumber()",
    "onError": "keep-original",
    "repeat": false,
    "repeatCount": 10
  },
  {
    "op": "core/text-transform",
    "description": "Text transform on cells in column gps_Accuracy using expression value.toNumber()",
    "engineConfig": {
      "facets": [],
      "mode": "row-based"
    },
    "columnName": "gps_Accuracy",
    "expression": "value.toNumber()",
    "onError": "keep-original",
    "repeat": false,
    "repeatCount": 10
  },
  {
    "op": "core/text-transform",
    "description": "Text transform on cells in column roof_type using expression value.toUppercase()",
    "engineConfig": {
      "facets": [],
      "mode": "row-based"
    },
    "columnName": "roof_type",
    "expression": "value.toUppercase()",
    "onError": "keep-original",
    "repeat": false,
    "repeatCount": 10
  },
  {
    "op": "core/text-transform",
    "description": "Text transform on cells in column wall_type using expression value.toUppercase()",
    "engineConfig": {
      "facets": [],
      "mode": "row-based"
    },
    "columnName": "wall_type",
    "expression": "value.toUppercase()",
    "onError": "keep-original",
    "repeat": false,
    "repeatCount": 10
  },
  {
    "op": "core/text-transform",
    "description": "Text transform on cells in column floor_type using expression value.toUppercase()",
    "engineConfig": {
      "facets": [],
      "mode": "row-based"
    },
    "columnName": "floor_type",
    "expression": "value.toUppercase()",
    "onError": "keep-original",
    "repeat": false,
    "repeatCount": 10
  },
  {
    "op": "core/text-transform",
    "description": "Text transform on cells in column no_membrs using expression value.toNumber()",
    "engineConfig": {
      "facets": [],
      "mode": "row-based"
    },
    "columnName": "no_membrs",
    "expression": "value.toNumber()",
    "onError": "keep-original",
    "repeat": false,
    "repeatCount": 10
  },
  {
    "op": "core/text-transform",
    "description": "Text transform on cells in column years_liv using expression value.toNumber()",
    "engineConfig": {
      "facets": [],
      "mode": "row-based"
    },
    "columnName": "years_liv",
    "expression": "value.toNumber()",
    "onError": "keep-original",
    "repeat": false,
    "repeatCount": 10
  }
]
