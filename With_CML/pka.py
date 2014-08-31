pka_patterns = OrderedDict()

pka_patterns["Alkane"] = (50, {"atoms": {
                                         "a1": "H",
                                         "a2": "H",
                                         "a3": "H",
                                         "a4": "H",
                                         "a5": "H",
                                         "a6": "H",
                                         "a7": "C",
                                         "a8": "C"
                                        },
                               "bonds": {
                                         "b1": ("a1", "a7", 1),
                                         "b2": ("a2", "a7", 1),
                                         "b3": ("a3", "a7", 1),
                                         "b4": ("a4", "a8", 1),
                                         "b5": ("a5", "a8", 1),
                                         "b6": ("a6", "a8", 1),
                                         "b7": ("a7", "a8", 1)
                                        }
                              }
                         )

pka_patterns["Alkene"] = (43, {"atoms": {
                                         "a1": "H",
                                         "a2": "H",
                                         "a3": "H",
                                         "a4": "H",
                                         "a5": "C",
                                         "a6": "C"
                                        },
                               "bonds": {
                                         "b1": ("a1", "a5", 1),
                                         "b2": ("a2", "a5", 1),
                                         "b3": ("a3", "a6", 1),
                                        "b4": ("a4", "a6", 1),
                                        "b5": ("a5", "a6", 2)
                                        }
                              }
                         )

pka_patterns["Hydrogen"] = (42, {"atoms": {
                                           "a1": "H",
                                           "a2": "H"
                                          },
				 "bonds": {
	                                   "b1": ("a1", "a2", 1)
                                          }
				}
			   )
			   
pka_patterns["Amine"] = (35, {"atoms": {
					"a1": "H",
					"a2": "H",
					"a3": "H",
					"a4": "N"
				       },
	                      "bonds": {
				        "b1": ("a1", "a4", 1),
					"b2": ("a2", "a4", 1),
					"b3": ("a3", "a4", 1)
				       }
			     }
		        )
		        
pka_patterns["Sulfoxide"] = (31, {"atoms": {
                                            "a1": "H",
                                            "a2": "H",
                                            "a3": "H",
                                            "a4": "H",
                                            "a5": "H",
                                            "a6": "H",
                                            "a7": "C",
                                            "a8": "C",
                                            "a9": "S",
                                            "a10": "O"
                                           },
                                  "bonds": {
                                            "b1": ("a1", "a7", 1),
                                            "b1": ("a2", "a7", 1),
                                            "b1": ("a3", "a7", 1),
                                            "b1": ("a4", "a8", 1),
                                            "b1": ("a5", "a8", 1),
                                            "b1": ("a6", "a8", 1),
                                            "b1": ("a7", "a9", 1),
                                            "b1": ("a8", "a9", 1),
                                            "b1": ("a9", "a10", 2),
                                           }
                                 }
                             )

pka_patterns["Alkyne"] = (25, {"atoms": {
                                         "a1": "H",
                                         "a2": "C",
                                         "a3": "C",
                                         "a4": "H"
                                        },
                               "bonds": {
                                         "b1": ("a1", "a2", 1),
                                         "b2": ("a2", "a3", 3),
                                         "b3": ("a3", "a4", 1),
                                        }
                              }
                         )
pka_patterns["Ester"] =
pka_patterns["Nitrile"] =
pka_patterns["Ketone"] =
pka_patterns["Aldehyde"] =
pka_patterns["Alcohol"] =
pka_patterns["Water"] =
pka_patterns["Malonates"] =
pka_patterns["Thiols"] =
pka_patterns["Protonated amines"] =
pka_patterns["Carboxylic acids"] =
pka_patterns["Hydrofluoric acid"] =
pka_patterns["sulfonic acid"] =
pka_patterns["hydronium ion"] =
pka_patterns["sulfuric acid"] =
pka_patterns["hydrochloric acid"] =
pka_patterns["hydrobromic acid"] =
pka_patterns["hydroiodic acid"] =
