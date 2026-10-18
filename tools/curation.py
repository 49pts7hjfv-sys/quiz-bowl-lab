"""Curation rules for the coach's expanded study list (October 2026).

The expanded spreadsheet has one master list per content area (pulled from QBReader's frequency
data), so it repeats entries, spells the same answer several ways, and includes rows that are not
study topics. These rules turn every entry into exactly one of:

    -               drop it (junk row, generic word, mature content, or college-level only)
    =<id>           already a topic on the site (the 215 original topics are never changed)
    Name            a new topic called Name, in the list's own area
    Area: Name      a new topic in a different area (e.g. "The Jungle" on the history list)

Entries are matched after normalization (lowercase, no accents/punctuation, leading "the" dropped).
An entry with no rule becomes a new topic named after the entry, in the list's area. The Science
list mixes every science, so each of its entries is assigned explicitly (SCIENCE_AREAS).

No student names appear here: lists are identified by content area only.
"""

# Area each master list belongs to by default.
LIST_AREA = {
    "us": "American History",
    "eu": "European History",
    "lit": "Literature",
    "litc": "Literature",
    "myth": "Mythology",
    "rel": "Religion",
    "phil": "Philosophy",
    "soc": "Social Science",
    "fa": "Fine Arts",
    "mus": "Music",
    "sci": None,          # every entry assigned in SCIENCE_AREAS
    "astro": "Astronomy",
    "biomath": "Biology",  # entries from "Prime numbers" on are Math (see BIOMATH_MATH_FROM)
    "earth": "Earth Science",
}
BIOMATH_MATH_FROM = "Prime numbers"

RULES = {}

RULES["us"] = """
California
New York
Commonwealth of Massachusetts => Massachusetts
Reconstruction Era => Reconstruction
Richard Milhous Nixon => Richard Nixon
Henry Clay Sr. => Henry Clay
Harry Truman => Harry S. Truman
Susan Brownell Anthony => Susan B. Anthony
Boston, Massachusetts => Boston
attack on Pearl Harbor => Attack on Pearl Harbor
the attack on Pearl Harbor => Attack on Pearl Harbor
Pearl Harbor => Attack on Pearl Harbor
USS Arizona => Attack on Pearl Harbor
Cherokee Nation => Cherokee
tobacco => Tobacco
cotton => Cotton
filibuster => Filibuster
Lyndon Baines Johnson => Lyndon B. Johnson
Lyndon Johnson => Lyndon B. Johnson
Martin Luther King, Jr. => =martin-luther-king-jr
Dr. Martin Luther King, Jr. => =martin-luther-king-jr
I Have a Dream => =martin-luther-king-jr
Robert Edward Lee => Robert E. Lee
Supreme Court of the United States => U.S. Supreme Court
United States Supreme Court => U.S. Supreme Court
William Jefferson "Bill" Clinton => Bill Clinton
BillClinton => Bill Clinton
Barack Hussein Obama II => Barack Obama
Brown v. Board of Education of Topeka => Brown v. Board of Education
school desegregation => Brown v. Board of Education
Chicago, Illinois => Chicago
guns => Second Amendment
freedom of the press => First Amendment
Rhode Island and Providence Plantations => Rhode Island
abortion => Roe v. Wade
Ronald Wilson Reagan => Ronald Reagan
Ronald => Ronald Reagan
The Alamo => Battle of the Alamo
Theodore "Teddy" Roosevelt => =theodore-roosevelt
Theodore Roosevelt Jr. => =theodore-roosevelt
Thomas Woodrow Wilson => =woodrow-wilson
Articles of Confederation and Perpetual Union => Articles of Confederation
communism => Social Science: Communism
Socialism => Social Science: Socialism
David "Davy" Crockett => Davy Crockett
Dred Scott v. Sanford => Dred Scott v. Sandford
George Walker Bush => George W. Bush
the Great Depression => Great Depression
Hoovervilles => Great Depression
Kennedy => John F. Kennedy
John Fitzgerald Kennedy => John F. Kennedy
Kennedy family => John F. Kennedy
League of Nations => European History: League of Nations
Lee Harvey Oswald
Assassination of John Fitzgerald Kennedy => Lee Harvey Oswald
assassination of John F. Kennedy => Lee Harvey Oswald
Jack Leon Ruby => Lee Harvey Oswald
assassination of Abraham Lincoln => John Wilkes Booth
Scopes monkey trial => Scopes Trial
Soviet Union => European History: Soviet Union
9/11 attacks => September 11 attacks
alcohol => =prohibition
Antonio Lopez de Santa Anna => Antonio López de Santa Anna
assassination => -
Cabinet => Cabinet of the United States
Chester Alan Arthur => Chester A. Arthur
Haymarket Square Riot => Haymarket Affair
Ford Motor Company => Henry Ford
taxes => Income tax
income tax => Income tax
James Abram Garfield => James Garfield
James Earl "Jimmy" Carter => Jimmy Carter
John Davison Rockefeller => John D. Rockefeller
Standard Oil Company => John D. Rockefeller
labor strike => Labor unions
labor unions => Labor unions
Martin van Buren => Martin Van Buren
Montgomery => Montgomery, Alabama
Nero Claudius Caesar Augustus Germanicus => European History: Nero
Savannah => Savannah, Georgia
Shays' Rebellion => Shays’ Rebellion
slave revolt => Slave rebellions
Stamp Act of 1765 => Stamp Act
Stephen Douglas => Stephen A. Douglas
The Federalist Papers => The Federalist Papers
Federalist Papers => The Federalist Papers
The Jungle => Literature: The Jungle
The New Deal => New Deal
The Star-Spangled Banner => Francis Scott Key
Upton Sinclair => Literature: Upton Sinclair
Vicksburg => Siege of Vicksburg
19th Amendment => =womens-suffrage
abolitionism => Abolitionism
affirmative action => Affirmative action
African-Americans => -
Alan => -
Arlington County => Arlington National Cemetery
Bacon's Rebellion => Bacon’s Rebellion
Battle of Iwo Jima => Battle of Iwo Jima
Iwo Jima => Battle of Iwo Jima
Battle of Lexington => Battles of Lexington and Concord
Battle of the Bulge => European History: Battle of the Bulge
Camp David => Camp David Accords
checks and balances => Checks and balances
Christopher Columbus => European History: Christopher Columbus
Don't Ask, Don't Tell => Don’t Ask, Don’t Tell
Dwight David Eisenhower => Dwight D. Eisenhower
eminent domain => Eminent domain
evolution of humans => Biology: Human evolution
federalism => Federalism
Gabrielle "Gabby" Giffords => Gabby Giffords
George => -
George Gordon Meade => George Meade
Great Chicago Fire of 1871 => Great Chicago Fire
Greece => -
Harpers Ferry => John Brown
Honolulu => Hawaii
Herbert => Herbert Hoover
Herbert Clark Hoover => Herbert Hoover
Hillary Rodham Clinton => Hillary Clinton
internment of Japanese-Americans => Japanese American internment
Japanese-Americans => Japanese American internment
ironclads => Ironclads
James Strom Thurmond => Strom Thurmond
Jamestown, Virginia => =jamestown
Jim Crow => Jim Crow laws
John Glover Roberts, Jr. => John Roberts
Julius Robert Oppenheimer => J. Robert Oppenheimer
Kansas-Nebraska Act of 1854 => Kansas–Nebraska Act
Kent State University => Kent State shootings
King Philip's War => King Philip’s War
Meriwether Lewis and William Clark => Lewis and Clark Expedition
Lincoln Memorial => =lincoln-memorial
Lord Charles Cornwallis => Charles Cornwallis
marriage => -
Newton "Newt" Gingrich => Newt Gingrich
Patient Protection and Affordable Care Act => Affordable Care Act
Pickett's Charge => =battle-of-gettysburg
Saint Augustine => St. Augustine, Florida
same-sex marriage => Same-sex marriage
sinking of the RMS Titanic => European History: Sinking of the Titanic
State Department => Secretary of State
steamboat => Robert Fulton
Suez Canal => European History: Suez Canal
supremacy clause => Supremacy Clause
the draft => Military draft
veto => Veto
impeachment => Impeachment
executive branch => Executive branch
"""

RULES["eu"] = """
Kingdom of Spain => Spain
Republic of Poland => Poland
Kingdom of Poland => Poland
Ireland => Republic of Ireland
Republic of Ireland => Republic of Ireland
Louis => -
Kingdom of Portugal => Portugal
assassination of Archduke Franz Ferdinand => =archduke-franz-ferdinand
Empire ofAustria => Austria
cosmonauts => Cosmonauts
the European Union => European Union
Kingdom of France => France
Henry => -
King Henry VIII Tudor => =henry-viii
Henry VIII Tudor of England => =henry-viii
King Henry VIII => =henry-viii
London, England => London
Pope => The Pope
popes => The Pope
Pope of the Roman Catholic Church => The Pope
Queen Elizabeth I => =elizabeth-i
Queen Elizabeth I of Tudor => =elizabeth-i
Elizabeth => -
The Soviet Union => Soviet Union
USSR => Soviet Union
Kingdom of Sweden => Sweden
The Netherlands => Netherlands
Netherlands => Netherlands
Treaty ofVersailles => Treaty of Versailles
William I => William the Conqueror
Antarctica => -
the Black Death => Black Death
Byzantine Empire or Byzantium => Byzantine Empire
Canada => -
Constantinople or Istanbul => Constantinople
French and Indian War => American History: French and Indian War
Galileo Galilei => Physics: Galileo Galilei
Federal Republic of Germany => Germany
Grigori Yefimovich Rasputin => Grigori Rasputin
Isabella I => Isabella I of Castile
Isabella of Castile => Isabella I of Castile
Ivan => Ivan the Terrible
Ivan IV => Ivan the Terrible
Kingdom of Belgium => Belgium
Kingdom of Norway => Norway
Magna Carta => =magna-carta
Maximilien Francois Marie Isidore de Robespierre => Maximilien Robespierre
Peter I => =peter-the-great
Pisa => -
Republic of Venice => Venice
Kingdom of Scotland => Scotland
Sir Winston Leonard Spencer-Churchill => =winston-churchill
Sir Winston Churchill => =winston-churchill
The Holocaust => The Holocaust
Auschwitz II-Birkenau => The Holocaust
genocide => -
2nd Punic War => Second Punic War
abdication => -
African slaves => -
slaves => -
Arthur Neville Chamberlain => Neville Chamberlain
Catherine II of Russia => =catherine-the-great
Catherine the Great or Catherine II => =catherine-the-great
Charlemagne or Charles I or Carolus Magnus or Charles the Great => =charlemagne
Chernobyl Nuclear Power Plant => Chernobyl disaster
Chernobyl nuclear reactor explosion => Chernobyl disaster
China => -
Christianity => Religion: Christianity
Cleopatra VII Philopator => Cleopatra
Constantine => Constantine the Great
First Council of Nicaea => Council of Nicaea
First Crusade => =crusades
Francisco Franco Bahamonde => Francisco Franco
Frederick II => Frederick the Great
Friedrich Engels => Philosophy: Friedrich Engels
George III Hanover => George III
Gustavus Adolphus or Gustav II Adolf of Sweden => Gustavus Adolphus
Habsburg => House of Habsburg
Habsburg Dynasty => House of Habsburg
House of Hapsburg => House of Habsburg
Huns => =attila-the-hun
James I => James I of England
Joan of Arc => =joan-of-arc
Joaquin Archivaldo Guzman Loera => -
Josef Stalin => =joseph-stalin
Justinian I => Justinian I
King Louis XVI => Louis XVI
Kingdom of Prussia => Prussia
Libya => -
Mary => -
monarchy => -
New York City => -
New Zealand => -
Otto Eduard Leopold von Bismarck => =otto-von-bismarck
Panama Canal => American History: Panama Canal
Peasants' Revolts => Peasants’ Revolt
Queen Alexandrina Victoria => =queen-victoria
Victoria of the United Kingdom => =queen-victoria
Richard I => Richard the Lionheart
RMS Lusitania => Sinking of the Lusitania
Romanov dynasty or family => Romanov dynasty
Russian Federation => Russia
serfs => Serfdom
Stamp Act of 1765 => American History: Stamp Act
The Bastille => Storming of the Bastille
The Communist Manifesto => Philosophy: The Communist Manifesto
The Diary of a Young Girl => Literature: The Diary of a Young Girl
The Prince => =the-prince
The Thirty Years' War => =thirty-years-war
train transportation => -
Tsar => Tsar
Tsar Nicholas II => Nicholas II
Vladimir Ilyich Lenin => Vladimir Lenin
War of Austrian Succession => War of the Austrian Succession
Alfred Nobel => Alfred Nobel
League of Nations => League of Nations
Soviet Union => Soviet Union
Battle of the Bulge => Battle of the Bulge
Christopher Columbus => Christopher Columbus
Greece => Greece
"""

RULES["lit"] = """
Inferno => =the-divine-comedy
Inferno (Dante) => =the-divine-comedy
Divine Comedy => =the-divine-comedy
Lolita => -
Japan => -
Poland => -
Portugal => -
Argentina => -
Chile => -
Spanish => -
Charge of the Light Brigade => The Charge of the Light Brigade
St. Francis College => -
My Antonia => My Ántonia
1984.0 => =nineteen-eighty-four
Huckleberry Finn => Adventures of Huckleberry Finn
Romeo => =romeo-and-juliet
Republic => Philosophy: The Republic
The Overcoat (1926 film) => The Overcoat
Scheherazade => One Thousand and One Nights
The Secret Life of Walter Mitty (1947 film) => James Thurber
Ichabod - The Legend of Sleepy Hollow (Decca album) => The Legend of Sleepy Hollow
Night => Night (Elie Wiesel)
Jay Gatsby => =the-great-gatsby
Alice => Alice’s Adventures in Wonderland
Father and Son => Fathers and Sons
Awakening => The Awakening
Hansel and Gretel => Brothers Grimm
Diary => The Diary of a Young Girl
The Dumb Waiter => Harold Pinter
Grendel => Grendel
Sonnet => Sonnet
Oedipus the King => =oedipus-rex
Bridge => -
The Lottery Man (1919 film) => The Lottery
Holden Caulfield => =the-catcher-in-the-rye
Ghost => -
The Second Coming (Kiss video) => The Second Coming
Bride of Frankenstein => Frankenstein
Atticus Finch => =to-kill-a-mockingbird
Simone Martini => -
Rosencrantz and Guildenstern => Rosencrantz and Guildenstern Are Dead
Plato => =plato
The Prince => =the-prince
Le Morte d'Arthur => Le Morte d’Arthur
The Gift of the Magi => O. Henry
Frank Lloyd Wright => Fine Arts: Frank Lloyd Wright
Tiresias => Mythology: Tiresias
Epic poetry => Epic poetry
Javert => =les-miserables
Odysseus => Mythology: Odysseus
Tom Sawyer => =the-adventures-of-tom-sawyer
Mrs Dalloway => Mrs. Dalloway
Puck => =a-midsummer-nights-dream
Paul Revere's Ride => Paul Revere’s Ride
Sword => -
Jean-Paul Sartre => Philosophy: Jean-Paul Sartre
Upton Sinclair => Upton Sinclair
The Jungle => The Jungle
The Diary of a Young Girl => The Diary of a Young Girl
Gulliver's Travels => Gulliver’s Travels
A Doll's House => A Doll’s House
The Pilgrim's Progress => The Pilgrim’s Progress
Eugene O'Neill => Eugene O’Neill
Flannery O'Connor => Flannery O’Connor
Uncle Tom's Cabin => Uncle Tom’s Cabin
Who's Afraid of Virginia Woolf? => Who’s Afraid of Virginia Woolf?
Tess of the d'Urbervilles => Tess of the d’Urbervilles
A Connecticut Yankee in King Arthur's Court => A Connecticut Yankee in King Arthur’s Court
The Handmaid's Tale => The Handmaid’s Tale
Rubaiyat of Omar Khayyam => Rubáiyát of Omar Khayyám
Kenzaburo Oe => Kenzaburō Ōe
Death Comes for the Archbishop => Death Comes for the Archbishop
"""

RULES["litc"] = """
Gaius Valerius Catullus => Catullus
Catullus => Catullus
Lesbia => Catullus
Sappho of Lesbos => Sappho
Medea => Mythology: Medea
the Wasps => The Wasps
Publius Ovidius Naso => Ovid
Titus Maccius Plautus => Plautus
Miles Gloriosus => Plautus
Marcus Valerius Martialis => Martial
Peace => Aristophanes
The Knights => Aristophanes
The Clouds => The Clouds
Latin => -
Ancient Greek => -
The Aeneid => =aeneid
Oedipus Rex => =oedipus-rex
satyr plays => Satyr play
Odysseus => Mythology: Odysseus
Publius Papinius Statius => Statius
Sextus Propertius => Propertius
tragedy => Greek tragedy
Aphrodite => Mythology: Aphrodite
catharsis => Catharsis
"""

RULES["myth"] = """
Aztec => Aztec mythology
Phoebus Apollo => =apollo
Titan => Titans
Inca Empire => Inca mythology
Shinto => Religion: Shinto
Kami => Religion: Shinto
Labours of Hercules => =heracles
Hercules => =heracles
The Hydra => =heracles
Le Morte d'Arthur => Literature: Le Morte d’Arthur
Moon => -
The Green Magician => -
Wind => -
Green Knight => Literature: Sir Gawain and the Green Knight
Dwarf => Dwarves (Norse mythology)
Ancient Egyptian deities => Egyptian mythology
Grendel => Literature: Grendel
Goliath => Religion: King David
Maui-tikitiki => Maui
Mjölnir => =thor
Venus => Aphrodite
Muse => Muses
Argonauts => =jason
Pendragon => King Arthur
Unicorn => -
Maya => Maya mythology
Valkyrie => Valkyries
Cynic => -
Oracle => Oracle of Delphi
Babylon => -
Centaur => Centaurs
Ravens => =odin
Athens => European History: Athens
Trojan Horse => Trojan War
Four Winds => -
Heimdallr => Heimdall
Proioxis => -
Cú Chulainn => =cu-chulainn
Ragnarök => Ragnarök
"""

RULES["rel"] = """
Shintoism => Shinto
Mary => Mary, mother of Jesus
baptism => Baptism
Church of Scientology => Scientology
Gabriel => Gabriel (archangel)
Joseph => Joseph (son of Jacob)
karma => Karma
meditation => Meditation
prayer => Prayer
reincarnation => Reincarnation
Saint Paul the Apostle => Paul the Apostle
Baha'i Faith => =bahai-faith
"""

RULES["phil"] = """
pragmatism => Pragmatism
ethics => Ethics
knowledge => Epistemology
free will => Free will
truth => Truth
justice => Justice
skepticism => Skepticism
logic => Logic
Soren Kierkegaard => Søren Kierkegaard
Soren Aabye Kierkegaard => Søren Kierkegaard
Friedrich Wilhelm Nietzsche => Friedrich Nietzsche
Confucianism => =confucius
history => -
science => -
atoms => Atomism
"""

RULES["soc"] = """
Emile Durkheim => Émile Durkheim
suicide => Émile Durkheim
Claude Levi-Strauss => Claude Lévi-Strauss
Bronislaw Malinowski => Bronisław Malinowski
personality => Personality
memory => Memory
intelligence => Intelligence
vowels => Vowels
emotions => Emotions
Stanford University => -
crime => -
Taxes => Taxation
capital => Capital
Carl Gustav Jung => Carl Jung
Bystander effect => Bystander effect
cognitive dissonance => Cognitive dissonance
culture => Culture
voting => Voting
conformity => Conformity
cities => -
utility => Utility
money => Money
Philip Zimbardo => =stanford-prison-experiment
risk => -
schizophrenia => Schizophrenia
"""

RULES["fa"] = """
Salvador Dali => Salvador Dalí
Albrecht Durer => Albrecht Dürer
Constantin Brancusi => Constantin Brâncuși
Paul Cezanne => Paul Cézanne
Edouard Manet => Édouard Manet
Eugene Delacroix => Eugène Delacroix
Diego Velazquez => Diego Velázquez
Rene Magritte => René Magritte
Japan => -
Mexico => -
Michelangelo Merisi da Caravaggio => Caravaggio
David => David (Michelangelo)
"""

RULES["mus"] = """
Frederic Chopin => Frédéric Chopin
Bela Bartok => Béla Bartók
Camille Saint-Saens => Camille Saint-Saëns
Antonin Dvorak => Antonín Dvořák
Niccolo Paganini => Niccolò Paganini
"""

# Science master list: every entry assigned to an area ("raw => Name" renames).
SCIENCE_AREAS = {
"=": """
Mitochondrion => =mitochondria
Glacier => =glaciers
Quartz => =quartz
Endoplasmic reticulum => =endoplasmic-reticulum
Meiosis => =meiosis
Black hole => =black-holes
Cell membrane => =cell-membrane
Liver => =liver
Electron => =electrons
Mantle => =mantle
Volcano => =volcanoes
Refractive index => =refraction
Stomach => =stomach
Laser => =lasers
Nucleus => =nucleus
Tornado => =tornadoes
Heart => =heart
Photosynthesis => =photosynthesis
Fungus => =fungi
Lung => =lungs
Limestone => =limestone
Neuron => =neurons
Brain => =brain
Kidney => =kidneys
DNA => =dna
Glucose => =glucose
Ribosome => =ribosomes
Cloud => =clouds
Cumulonimbus cloud => =clouds
Tropical cyclone => =hurricanes
Gravitational constant => =gravity
Wavelength => =waves
Principia Mathematica => =isaac-newton
""",
"-": """
Ether
Inverse
String
Virtual
Volume
Beta-Hydride elimination
""",
"Physics": """
Entropy
Doppler effect
Angular momentum
Nuclear fusion
Viscosity
Plasma => Plasma (physics)
Temperature
Momentum
Potential energy
Surface tension
Superconductivity
Capacitor => Capacitors
Capacitance => Capacitors
Enrico Fermi
Ferromagnetism
Pendulum => Pendulums
Electrical resistance and conductance => Electrical resistance
Resistor => Electrical resistance
Weak interaction => Weak nuclear force
Scattering
Uncertainty principle
Electric field
Neutrino => Neutrinos
Magnetic field => Magnetic fields
Pauli exclusion principle
Michael Faraday
Reflection
Diffraction
Proton => Protons
Bernoulli's principle => Bernoulli’s principle
Hall effect
Brownian motion
Absolute zero
Michelson-Morley experiment => Michelson–Morley experiment
Higgs boson
Neutron => Neutrons
Torque
Power => Power (physics)
Richard Feynman
Heat capacity
Second law of thermodynamics
Newton's laws of motion => Newton’s laws of motion
Max Planck
Resonance
X-ray => X-rays
Electric current
Current => Electric current
Electric charge
Hooke's law => Hooke’s law
Relativity => Theory of relativity
Special relativity => Theory of relativity
Simple machine => Simple machines
Diode => Diodes
Ampère's circuital law => Ampère’s law
Spin => Spin (physics)
Gustav Kirchhoff
Maxwell's demon => Maxwell’s demon
John William Strutt => Lord Rayleigh
Oil drop experiment => Millikan oil drop experiment
Magnetic monopole => Magnetic monopoles
Density
Drag => Drag (physics)
Semiconductor => Semiconductors
Convection
Coulomb's law => Coulomb’s law
Charles-Augustin de Coulomb => Coulomb’s law
Magnetism
Antimatter
Antiparticle => Antimatter
Voltage
Gauss's law => Gauss’s law
Bose-Einstein condensate => Bose–Einstein condensate
Melting
Work => Work (physics)
Tension => Tension (physics)
Liquid => Liquids
Precession
Niels Bohr
""",
"Chemistry": """
Electronegativity
Avogadro constant => Avogadro’s number
Halogen => Halogens
Hydrogen
Carbon
Titration
Distillation
Boron
Noble gas => Noble gases
Ideal gas law
Ideal gas => Ideal gas law
Water
Enthalpy
Colloid => Colloids
Sulfur
Chromatography
Hydrogen bond => Hydrogen bonds
Alcohol => Alcohols (chemistry)
Gibbs free energy
Calcium
Benzene
Lead => Lead (element)
Fluorine
Ammonia
Carbon dioxide
Helium
Acid => Acids
Van der Waals force => Van der Waals forces
Lanthanide => Lanthanides
Henry's law => Henry’s law
Ion => Ions
Copper
Nitrogen
Vapor pressure
Sulfuric acid
Boiling point
Curie => Marie Curie
Solubility
Redox
Reduction => Redox
Infrared spectroscopy
Lattice energy
Potassium
Titanium
Boyle's law => Boyle’s law
Atomic orbital => Atomic orbitals
Chemical equilibrium
Equilibrium constant => Chemical equilibrium
Oxygen
Ester => Esters
Electrolyte => Electrolytes
Haber process
Alkene => Alkenes
Acetic acid
Sodium
Robert Bunsen
Polymer => Polymers
Phosphorus
Methane
Catalysis => Catalysts
Aluminium => Aluminum
Activation energy
Chlorine
PH => pH
Electrolysis
Gold
Flame test
Diels-Alder Reaction => Diels–Alder reaction
Linus Pauling
Electrode => Electrodes
Gas constant
Reaction rate
Dipole => Dipoles
Molecular orbital theory
""",
"Biology": """
Echinoderm => Echinoderms
Diffusion
Mollusca => Mollusks
Retina
Golgi apparatus
Malaria
Chloroplast => Chloroplasts
Small intestine
Lysosome => Lysosomes
Light-independent reactions => Calvin cycle
Cnidaria => Cnidarians
Vitamin C
Glycolysis
HIV
HIV/AIDS => HIV
Pancreas
Stem cell => Stem cells
Phloem
Transcription
Enzyme => Enzymes
Cholesterol
RNA
Leaf => Leaves
Epinephrine => Epinephrine (adrenaline)
Parkinson's disease => Parkinson’s disease
Leprosy
Charles Darwin
Amino acid => Amino acids
Species
Keratin
Gallbladder
Stamen
Nematode => Nematodes
ATP
Platelet => Platelets
Escherichia coli => E. coli
Prophase => Mitosis
Anaphase => Mitosis
Yeast
Sickle-cell disease => Sickle-cell disease
Cartilage
Pituitary gland
Neanderthal => Neanderthals
Serotonin
Orthomyxoviridae => Influenza virus
Antibody => Antibodies
Gymnosperm => Gymnosperms
Adrenal gland => Adrenal glands
Coagulation => Blood clotting
Thyroid => Thyroid gland
Conjugation => Bacterial conjugation
Testosterone
Coral reef => Coral reefs
Diabetes mellitus => Diabetes
Bird => Birds
Honey bee => Honey bees
Carrying capacity
Actin
Capillary => Capillaries
Down syndrome
Tree => Trees
Pulmonary alveolus => Alveoli
Root => Roots
Active transport
Tooth => Teeth
Bacteriophage => Bacteriophages
Glycine
Muscle => Muscles
Louis Pasteur
B vitamins
Vacuole => Vacuoles
Sponge => Sponges
Hemoglobin
Operon => Lac operon
Cancer
Mutation => Mutations
Collagen
Virus => Viruses
Insulin
Peroxisome => Peroxisomes
X chromosome
Cochlea
Lactic acid
Maize => Corn (maize)
Red blood cell => Red blood cells
White blood cell => White blood cells
Fats => Lipids
Fruit fly => Fruit flies
Cilium => Cilia
Sleep
Vitamin => Vitamins
Xylem
Homo => Human evolution
Cholera
Spleen
Cerebrum
Epidermis => Skin
DNA sequencing
Pheromone => Pheromones
Placenta
Bone => Bones
Pea => Gregor Mendel
Speciation
Alzheimer's disease => Alzheimer’s disease
""",
"Earth Science": """
Seafloor spreading
Fault => Faults
Coriolis force => Coriolis effect
Feldspar
Subduction
Jurassic => Jurassic period
Cambrian => Cambrian period
Stratosphere
Plate tectonics
Tide => Tides
Mesozoic => Mesozoic Era
Desert => Deserts
Wind
Aquifer => Aquifers
Hardness => Mohs hardness scale
El Niño
Plagioclase
Soil
Lightning
Ozone => Ozone layer
Cretaceous => Cretaceous period
Granite
Ionosphere
Geyser => Geysers
Mohorovicic discontinuity => Mohorovičić discontinuity
Magma
Ocean => Oceans
Core => Earth’s core
Van Allen radiation belt => Van Allen radiation belts
Diamond
Condensation
""",
"Astronomy": """
Orion
Comet => Comets
Neptune
Jupiter
Supernova => Supernovae
Mars
Galaxy => Galaxies
Mercury => Mercury (planet)
Venus => Venus (planet)
Saturn
Johannes Kepler
Kepler's laws of planetary motion => Johannes Kepler
Pluto
Sun => The Sun
Sunspot => Sunspots
Moon => The Moon
Sagittarius
Pulsar => Pulsars
Nebula => Nebulae
Kuiper belt => Kuiper Belt
Titan => Titan (moon)
Triton
Edwin Hubble
White dwarf => White dwarfs
Crab Nebula
Asteroid => Asteroids
Asteroid belt => Asteroids
Dark matter
Quasar => Quasars
Neutron star => Neutron stars
Star => Stars
Andromeda => Andromeda Galaxy
""",
"Math": """
Prime number => Prime numbers
Factorization => Prime numbers
Leonhard Euler
Fibonacci number => Fibonacci sequence
Trigonometric functions
Sine => Trigonometric functions
Euclid
Triangle => Triangles
Equilateral triangle => Triangles
Circle => Circles
Diameter => Circles
Factorial
Pi
Pythagorean theorem
Matrix => Matrices
Determinant
Carl Friedrich Gauss
Polynomial => Polynomials
Zero of a function => Polynomials
Fractal => Fractals
Function => Functions (math)
Normal distribution
Derivative => Derivatives
Pierre de Fermat
1 (number) => The number one
Fermat's Last Theorem => Fermat’s Last Theorem
Integration => Integrals
Vector => Vectors
System of linear equations => Systems of linear equations
Mean
Parallelogram => Parallelograms
Parabola => Parabolas
Sphere => Spheres
Greatest common divisor
Multiplication
Infinity
Integer => Integers
Logarithm => Logarithms
Natural logarithm => Logarithms
Complex number => Complex numbers
Hyperbola => Hyperbolas
Angles
Möbius strip
Parallel postulate
Square root => Square roots
Perfect number => Perfect numbers
Negative number => Negative numbers
Inequality => Inequalities
""",
"Computer Science": """
Recursion
Alan Turing
Java => Java (programming language)
Encryption
Central processing unit => Central processing unit (CPU)
Linux
Binary number => Binary numbers
Programming language => Programming languages
Quantum computing
Linked list => Linked lists
Bit => Bits (computing)
""",
"Social Science": """
Memory
Vowel => Vowels
Attention
Autism
""",
}

RULES["astro"] = """
black holes => =black-holes
Comets => Comets
dark matter => Dark matter
neutron stars => Neutron stars
neutron star => Neutron stars
Quasars => Quasars
Supernovae => Supernovae
Cosmic Microwave Background Radiation => Cosmic microwave background
Hertzsprung-Russell diagram => Hertzsprung–Russell diagram
Galaxies => Galaxies
elliptical galaxies => Galaxies
spiral galaxies => Galaxies
luminosity => Luminosity
asteroids => Asteroids
Mercury => Mercury (planet)
exoplanets => Exoplanets
Venus => Venus (planet)
Titan => Titan (moon)
Pulsars => Pulsars
Hydrogen => Chemistry: Hydrogen
helium => Chemistry: Helium
main sequence => Main sequence
White Dwarf => White dwarfs
white dwarfs => White dwarfs
the Sun => The Sun
Big Bang => Big Bang
distance => -
Cepheid variables => Cepheid variables
Edgeworth-Kuiper belt => Kuiper Belt
sunspots => Sunspots
star formation => Star formation
radio waves => Physics: Radio waves
gravitational lensing => Gravitational lensing
nebulae => Nebulae
Opik-Oort cloud => Oort cloud
stars => Stars
"""

RULES["biomath"] = """
pollen => Pollen
viruses => Viruses
amino acids => Amino acids
cancer => Cancer
cholesterol => Cholesterol
lysosomes => Lysosomes
xylem => Xylem
blood => Blood
cytokinesis => Mitosis
double helix => =dna
enzymes => Enzymes
malaria => Malaria
mitosis => Mitosis
red blood cells => Red blood cells
skin => Skin
sleep => Sleep
adrenaline => Epinephrine (adrenaline)
birds => Birds
calcium => Chemistry: Calcium
chloroplasts => Chloroplasts
hemoglobin => Hemoglobin
insulin => Insulin
natural selection => =evolution
pancreas => Pancreas
plants => Plants
poliomyelitis => Polio
predators => Predation
proteins => Proteins
Punnett square => Punnett squares
roots => Roots
teeth => Teeth
transcription => Transcription
tundra => Tundra
Alzheimer's disease => Alzheimer’s disease
apoptosis => Apoptosis
cellulose => Cellulose
cystic fibrosis => Cystic fibrosis
Escherichia coli => E. coli
flowers => Flowers
Kidney => =kidneys
serotonin => Serotonin
small intestine => Small intestine
snakes => Snakes
stamen => Stamen
thylakoids => Thylakoids
uracil => Uracil
water => Chemistry: Water
anaphase => Mitosis
bacteria => Bacteria
blood type => Blood types
chlorophyll => Chlorophyll
Chordata => Chordates
coral reefs => Coral reefs
diffusion => Diffusion
dopamine => Dopamine
duodenum => Small intestine
Echinodermata => Echinoderms
food chains => Food chains
genetic drift => Genetic drift
heterozygous => Punnett squares
hormones => Hormones
interphase => Mitosis
keratin => Keratin
leaves => Leaves
lipids => Lipids
marsupials => Marsupials
metamorphosis => Metamorphosis
mushrooms => =fungi
nephron => =kidneys
nucleotides => Nucleotides
penicillin => Penicillin
potassium => Chemistry: Potassium
prions => Prions
Prime numbers => Math: Prime numbers
Leonhard Euler => Math: Leonhard Euler
integration => Math: Integrals
polynomials => Math: Polynomials
factorial => Math: Factorial
determinant => Math: Determinant
Pierre de Fermat => Math: Pierre de Fermat
zero => Math: Zero
fractals => Math: Fractals
pi => Math: Pi
complex numbers => Math: Complex numbers
matrix => Math: Matrices
Matrices => Math: Matrices
normal distribution => Math: Normal distribution
Fermat's Last Theorem => Math: Fermat’s Last Theorem
Continuity => Math: Continuity
David Hilbert => Math: David Hilbert
one => Math: The number one
standard deviation => Math: Standard deviation
variance => Math: Standard deviation
Augustin-Louis Cauchy => Math: Augustin-Louis Cauchy
Carl Friedrich Gauss => Math: Carl Friedrich Gauss
groups => Math: Group theory
Sets => Math: Set theory
integers => Math: Integers
eigenvalues => Math: Eigenvalues
four => Math: The number four
cosine => Math: Trigonometric functions
sine => Math: Trigonometric functions
Euclid => Math: Euclid
Pythagorean theorem => Math: Pythagorean theorem
real numbers => Math: Real numbers
Bernhard Riemann => Math: Bernhard Riemann
differentiation => Math: Derivatives
derivative => Math: Derivatives
permutations => Math: Permutations
Rational numbers => Math: Rational numbers
two => Math: The number two
vectors => Math: Vectors
compactness => -
Graphs => Math: Graph theory
triangles => Math: Triangles
circle => Math: Circles
circles => Math: Circles
Convergence => Math: Convergence (series)
Mean => Math: Mean
spheres => Math: Spheres
Georg Cantor => Math: Georg Cantor
Taylor series => Math: Taylor series
commutativity => Math: Commutative property
"""

RULES["earth"] = """
glaciers => =glaciers
Quartz => =quartz
Mantle => =mantle
Clouds => =clouds
Volcanoes => =volcanoes
soil => Soil
Seafloor Spreading => Seafloor spreading
feldspars => Feldspar
moraines => Moraines
tides => Tides
aquifers => Aquifers
stratosphere => Stratosphere
granite => Granite
tectonic plates => Plate tectonics
igneous rocks => Igneous rocks
iron => Chemistry: Iron
rivers => Rivers
asthenosphere => Asthenosphere
lava => Magma
magma => Magma
Mohorovicic Discontinuity => Mohorovičić discontinuity
ocean currents => Ocean currents
Bowen's reaction series => Bowen’s reaction series
olivine => Olivine
salinity => Salinity
Earth's magnetic field => Earth’s magnetic field
troposphere => Troposphere
ozone => Ozone layer
upwelling => Upwelling
water => Chemistry: Water
Faults => Faults
Jurassic period => Jurassic period
subduction => Subduction
Temperature => Physics: Temperature
Cambrian Period => Cambrian period
El Nino => El Niño
obsidian => Obsidian
Lakes => Lakes
sand => Sand
ice => Ice
Sedimentary rocks => Sedimentary rocks
shale => Shale
caves => Caves
"""

# Topics left out on purpose, with the reason (shown in the build log, never on the site).
LEFT_OUT_REASONS = {
    "Lolita": "mature subject matter; not suitable for 11–12-year-olds",
    "Joaquin Archivaldo Guzman Loera": "a drug-cartel leader; not a history study topic for this age",
    "Beta-Hydride elimination": "college-level chemistry",
    "compactness": "college-level math",
}
