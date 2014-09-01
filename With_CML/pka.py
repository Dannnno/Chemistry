# Data taken from
# http://masterorganicchemistry.files.wordpress.com/2010/06/pkas.jpg
from collections import OrderedDict


pka_patterns = OrderedDict()

pka_patterns["Alkane"] = (00, {"atoms": {
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

pka_patterns["Alkene"] = (00, {"atoms": {
                                          "a1": "H",
                                          "a2": "H",
                                          "a3": "H",
                                          "a4": "H",
                                          "a5": "C",
                                          "a6": "C"
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

pka_patterns["Hydrogen"] = (00, {"atoms": {
                                            "a1": "H",
                                            "a2": "H"
                                          },
                                 "bonds": {
                                            "b0": ("a1", "a2", 1)
                                          }
                                }
                           )

pka_patterns["Amine"] = (00, {"atoms": {
                                         "a1": "H",
                                         "a2": "H",
                                         "a3": "H",
                                         "a4": "N"
                                       },
                              "bonds": {
                                         "b0": ("a1", "a2", 1),
                                         "b1": ("a1", "a2", 1),
                                         "b2": ("a1", "a2", 1)
                                       }
                             }
                        )

pka_patterns["Sulfoxide"] = (00, {"atoms": {
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
                                             "b0": ("a1", "a2", 1),
                                             "b1": ("a1", "a2", 1),
                                             "b2": ("a1", "a2", 1),
                                             "b3": ("a1", "a2", 1),
                                             "b4": ("a1", "a2", 1),
                                             "b5": ("a1", "a2", 1),
                                             "b6": ("a1", "a2", 1),
                                             "b7": ("a1", "a2", 1),
                                             "b8": ("a1", "a2", 1)
                                           }
                                 }
                            )

pka_patterns["Alkyne"] = (00, {"atoms": {
                                          "a1": "H",
                                          "a2": "H",
                                          "a3": "C",
                                          "a4": "C"
                                        },
                               "bonds": {
                                          "b0": ("a1", "a2", 1),
                                          "b1": ("a1", "a2", 1),
                                          "b2": ("a1", "a2", 1)
                                        }
                              }
                         )

pka_patterns["Ester"] = (00, {"atoms": {
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
                                         "b0": ("a1", "a2", 1),
                                         "b1": ("a1", "a2", 1),
                                         "b2": ("a1", "a2", 1),
                                         "b3": ("a1", "a2", 1),
                                         "b4": ("a1", "a2", 1),
                                         "b5": ("a1", "a2", 1),
                                         "b6": ("a1", "a2", 1),
                                         "b7": ("a1", "a2", 1),
                                         "b8": ("a1", "a2", 1),
                                         "b9": ("a1", "a2", 1)
                                       }
                             }
                        )

pka_patterns["Nitrile"] = (00, {"atoms": {
                                           "a1": "H",
                                           "a2": "H",
                                           "a3": "H",
                                           "a4": "C",
                                           "a5": "C",
                                           "a6": "N"
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

pka_patterns["Ketone"] = (00, {"atoms": {
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
                                          "b0": ("a1", "a2", 1),
                                          "b1": ("a1", "a2", 1),
                                          "b2": ("a1", "a2", 1),
                                          "b3": ("a1", "a2", 1),
                                          "b4": ("a1", "a2", 1),
                                          "b5": ("a1", "a2", 1),
                                          "b6": ("a1", "a2", 1),
                                          "b7": ("a1", "a2", 1),
                                          "b8": ("a1", "a2", 1)
                                        }
                              }
                         )

pka_patterns["Aldehyde"] = (00, {"atoms": {
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

pka_patterns["Alcohol"] = (00, {"atoms": {
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

pka_patterns["Water"] = (00, {"atoms": {
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

pka_patterns["Malonates"] = (00, {"atoms": {
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

pka_patterns["Thiols"] = (00, {"atoms": {
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

pka_patterns["Protonated amines"] = (00, {"atoms": {
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

pka_patterns["Carboxylic acids"] = (00, {"atoms": {
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

pka_patterns["Hydrofluoric acid"] = (00, {"atoms": {
                                                     "a1": "H",
                                                     "a2": "F"
                                                   },
                                          "bonds": {
                                                     "b0": ("a1", "a2", 1)
                                                   }
                                         }
                                    )

pka_patterns["Hydronium ion"] = (00, {"atoms": {
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

pka_patterns["Sulfuric acid"] = (00, {"atoms": {
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

pka_patterns["Hydrochloric acid"] = (00, {"atoms": {
                                                     "a1": "H",
                                                     "a2": "l"
                                                   },
                                          "bonds": {
                                                     "b0": ("a1", "a2", 1)
                                                   }
                                         }
                                    )

pka_patterns["Hydrobromic acid"] = (00, {"atoms": {
                                                    "a1": "H",
                                                    "a2": "r"
                                                  },
                                         "bonds": {
                                                    "b0": ("a1", "a2", 1)
                                                  }
                                        }
                                   )

pka_patterns["Hydroiodic acid"] = (00, {"atoms": {
                                                   "a1": "H",
                                                   "a2": "I"
                                                 },
                                        "bonds": {
                                                   "b0": ("a1", "a2", 1)
                                                 }
                                       }
                                  )
