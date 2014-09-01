# Data taken from
# http://masterorganicchemistry.files.wordpress.com/2010/06/pkas.jpg
from collections import OrderedDict


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
                                          "b0": ("a1", "a7", 1),
                                          "b1": ("a2", "a7", 1),
                                          "b2": ("a3", "a7", 1),
                                          "b3": ("a4", "a8", 1),
                                          "b4": ("a5", "a8", 1),
                                          "b5": ("a6", "a8", 1),
                                          "b6": ("a7", "a8", 1)
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
                                          "b0": ("a1", "a5", 1),
                                          "b1": ("a2", "a5", 1),
                                          "b2": ("a3", "a6", 1),
                                          "b3": ("a4", "a6", 1),
                                          "b4": ("a5", "a6", 2)
                                        }
                              }
                         )

pka_patterns["Hydrogen"] = (42, {"atoms": {
                                            "a1": "H",
                                            "a2": "H"
                                          },
                                 "bonds": {
                                            "b0": ("a1", "a2", 1)
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
                                         "b0": ("a1", "a4", 1),
                                         "b1": ("a2", "a4", 1),
                                         "b2": ("a3", "a4", 1)
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
                                             "b0": ("a1", "a7", 1),
                                             "b1": ("a2", "a7", 1),
                                             "b2": ("a3", "a7", 1),
                                             "b3": ("a4", "a8", 1),
                                             "b4": ("a5", "a8", 1),
                                             "b5": ("a6", "a8", 1),
                                             "b6": ("a7", "a9", 1),
                                             "b7": ("a8", "a9", 1),
                                             "b8": ("a9", "a10", 2)
                                           }
                                 }
                            )

pka_patterns["Alkyne"] = (25, {"atoms": {
                                          "a1": "H",
                                          "a2": "H",
                                          "a3": "C",
                                          "a4": "C"
                                        },
                               "bonds": {
                                          "b0": ("a1", "a3", 1),
                                          "b1": ("a2", "a4", 1),
                                          "b2": ("a3", "a4", 1)
                                        }
                              }
                         )

pka_patterns["Ester"] = (25, {"atoms": {
                                         "a1": "H",
                                         "a2": "H",
                                         "a3": "H",
                                         "a4": "H",
                                         "a5": "H",
                                         "a6": "H",
                                         "a7": "C",
                                         "a8": "C",
                                         "a9": "C",
                                         "a10": "O",
                                         "a11": "O"
                                       },
                              "bonds": {
                                         "b0": ("a1", "a7", 1),
                                         "b1": ("a2", "a7", 1),
                                         "b2": ("a3", "a7", 1),
                                         "b3": ("a7", "a10", 1),
                                         "b4": ("a10", "a8", 1),
                                         "b5": ("a8", "a9", 1),
                                         "b6": ("a4", "a9", 1),
                                         "b7": ("a5", "a9", 1),
                                         "b8": ("a6", "a9", 1),
                                         "b9": ("a8", "a11", 1)
                                       }
                             }
                        )

pka_patterns["Nitrile"] = (25, {"atoms": {
                                           "a1": "H",
                                           "a2": "H",
                                           "a3": "H",
                                           "a4": "C",
                                           "a5": "C",
                                           "a6": "N"
                                         },
                                "bonds": {
                                           "b0": ("a1", "a4", 1),
                                           "b1": ("a2", "a4", 1),
                                           "b2": ("a3", "a4", 1),
                                           "b3": ("a4", "a5", 1),
                                           "b4": ("a5", "a6", 3)
                                         }
                               }
                          )

pka_patterns["Ketone"] = (20, {"atoms": {
                                          "a1": "H",
                                          "a2": "H",
                                          "a3": "H",
                                          "a4": "H",
                                          "a5": "H",
                                          "a6": "H",
                                          "a7": "C",
                                          "a8": "C",
                                          "a9": "C",
                                          "a10": "O"
                                        },
                               "bonds": {
                                          "b0": ("a1", "a7", 1),
                                          "b1": ("a2", "a7", 1),
                                          "b2": ("a3", "a7", 1),
                                          "b3": ("a4", "a9", 1),
                                          "b4": ("a5", "a9", 1),
                                          "b5": ("a6", "a9", 1),
                                          "b6": ("a7", "a8", 1),
                                          "b7": ("a9", "a8", 1),
                                          "b8": ("a9", "a10", 2)
                                        }
                              }
                         )

pka_patterns["Aldehyde"] = (19, {"atoms": {
                                            "a1": "H",
                                            "a2": "H",
                                            "a3": "H",
                                            "a4": "H",
                                            "a5": "C",
                                            "a6": "C",
                                            "a7": "O"
                                          },
                                 "bonds": {
                                            "b0": ("a1", "a2", 1),
                                            "b1": ("a1", "a2", 1),
                                            "b2": ("a1", "a2", 1),
                                            "b3": ("a1", "a2", 1),
                                            "b4": ("a1", "a2", 1),
                                            "b5": ("a1", "a2", 1)
                                          }
                                }
                           )

pka_patterns["Alcohol"] = (17, {"atoms": {
                                           "a1": "H",
                                           "a2": "H",
                                           "a3": "H",
                                           "a4": "H",
                                           "a5": "C",
                                           "a6": "O"
                                         },
                                "bonds": {
                                           "b0": ("a1", "a2", 1),
                                           "b1": ("a1", "a2", 1),
                                           "b2": ("a1", "a2", 1),
                                           "b3": ("a1", "a2", 1),
                                           "b4": ("a1", "a2", 1)
                                         }
                               }
                          )

pka_patterns["Water"] = (16, {"atoms": {
                                         "a1": "H",
                                         "a2": "H",
                                         "a3": "O"
                                       },
                              "bonds": {
                                         "b0": ("a1", "a2", 1),
                                         "b1": ("a1", "a2", 1)
                                       }
                             }
                        )

pka_patterns["Malonates"] = (13, {"atoms": {
                                             "a1": "H",
                                             "a2": "H",
                                             "a3": "H",
                                             "a4": "H",
                                             "a5": "H",
                                             "a6": "H",
                                             "a7": "H",
                                             "a8": "H",
                                             "a9": "C",
                                             "a10": "C",
                                             "a11": "C",
                                             "a12": "C",
                                             "a13": "C",
                                             "a14": "O",
                                             "a15": "O",
                                             "a16": "O",
                                             "a17": "O"
                                           },
                                  "bonds": {
                                             "b0": ("a1", "a2", 1),
                                             "b1": ("a1", "a2", 1),
                                             "b2": ("a1", "a2", 1),
                                             "b3": ("a1", "a2", 1),
                                             "b4": ("a1", "a2", 1),
                                             "b5": ("a1", "a2", 1),
                                             "b6": ("a1", "a2", 1),
                                             "b7": ("a1", "a2", 1),
                                             "b8": ("a1", "a2", 1),
                                             "b9": ("a1", "a2", 1),
                                             "b10": ("a1", "a2", 1),
                                             "b11": ("a1", "a2", 1),
                                             "b12": ("a1", "a2", 1),
                                             "b13": ("a1", "a2", 1),
                                             "b14": ("a1", "a2", 1),
                                             "b15": ("a1", "a2", 1)
                                           }
                                 }
                            )

pka_patterns["Thiols"] = (13, {"atoms": {
                                          "a1": "H",
                                          "a2": "H",
                                          "a3": "H",
                                          "a4": "H",
                                          "a5": "C",
                                          "a6": "S"
                                        },
                               "bonds": {
                                          "b0": ("a1", "a2", 1),
                                          "b1": ("a1", "a2", 1),
                                          "b2": ("a1", "a2", 1),
                                          "b3": ("a1", "a2", 1),
                                          "b4": ("a1", "a2", 1)
                                        }
                              }
                         )

pka_patterns["Protonated amines"] = (10, {"atoms": {
                                                     "a1": "H",
                                                     "a2": "H",
                                                     "a3": "H",
                                                     "a4": "H",
                                                     "a5": "N"
                                                   },
                                          "bonds": {
                                                     "b0": ("a1", "a2", 1),
                                                     "b1": ("a1", "a2", 1),
                                                     "b2": ("a1", "a2", 1),
                                                     "b3": ("a1", "a2", 1)
                                                   }
                                         }
                                    )

pka_patterns["Carboxylic acids"] = (04, {"atoms": {
                                                    "a1": "H",
                                                    "a2": "H",
                                                    "a3": "H",
                                                    "a4": "H",
                                                    "a5": "C",
                                                    "a6": "C",
                                                    "a7": "O",
                                                    "a8": "O"
                                                  },
                                         "bonds": {
                                                    "b0": ("a1", "a2", 1),
                                                    "b1": ("a1", "a2", 1),
                                                    "b2": ("a1", "a2", 1),
                                                    "b3": ("a1", "a2", 1),
                                                    "b4": ("a1", "a2", 1),
                                                    "b5": ("a1", "a2", 1),
                                                    "b6": ("a1", "a2", 1)
                                                  }
                                        }
                                   )

pka_patterns["Hydrofluoric acid"] = (3.2, {"atoms": {
                                                     "a1": "H",
                                                     "a2": "F"
                                                   },
                                          "bonds": {
                                                     "b0": ("a1", "a2", 1)
                                                   }
                                         }
                                    )

pka_patterns["Hydronium ion"] = (-1.7, {"atoms": {
                                                 "a1": "H",
                                                 "a2": "H",
                                                 "a3": "H",
                                                 "a4": "O"
                                               },
                                      "bonds": {
                                                 "b0": ("a1", "a2", 1),
                                                 "b1": ("a1", "a2", 1),
                                                 "b2": ("a1", "a2", 1)
                                               }
                                     }
                                )

pka_patterns["Sulfuric acid"] = (-3, {"atoms": {
                                                 "a1": "H",
                                                 "a2": "H",
                                                 "a3": "S",
                                                 "a4": "O",
                                                 "a5": "O",
                                                 "a6": "O",
                                                 "a7": "O"
                                               },
                                      "bonds": {
                                                 "b0": ("a1", "a2", 1),
                                                 "b1": ("a1", "a2", 1),
                                                 "b2": ("a1", "a2", 1),
                                                 "b3": ("a1", "a2", 1),
                                                 "b4": ("a1", "a2", 1),
                                                 "b5": ("a1", "a2", 1)
                                               }
                                     }
                                )

pka_patterns["Hydrochloric acid"] = (-6, {"atoms": {
                                                     "a1": "H",
                                                     "a2": "l"
                                                   },
                                          "bonds": {
                                                     "b0": ("a1", "a2", 1)
                                                   }
                                         }
                                    )

pka_patterns["Hydrobromic acid"] = (-9, {"atoms": {
                                                    "a1": "H",
                                                    "a2": "r"
                                                  },
                                         "bonds": {
                                                    "b0": ("a1", "a2", 1)
                                                  }
                                        }
                                   )

pka_patterns["Hydroiodic acid"] = (-10, {"atoms": {
                                                   "a1": "H",
                                                   "a2": "I"
                                                 },
                                        "bonds": {
                                                   "b0": ("a1", "a2", 1)
                                                 }
                                       }
                                  )
