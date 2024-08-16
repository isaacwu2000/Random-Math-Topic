# List of math topics
list_of_math_topics = [
    # Algebra
    "Exponent Laws",
    "Square Roots",
    "Fractional Exponents",
    "Evaluating Expressions",
    "Simplifying One-Variable Expressions",
    "One-Variable Distribution",
    "Ratios",
    "Unit Conversions",
    "Percents",
    "One-Variable Linear Equations",
    "Word Problems in One Variable",
    "Linear Equations in Disguise",
    "Graphing Lines",
    "Solving Linear Inequalities",
    "Solving Two-Variable Systems",
    "Two-Variable Word Problems",
    "Systems of Equations",
    "Direct Proportion",
    "Inverse Proportion",
    "Rate Problems",
    "Multiplying Binomials",
    "Factoring Monic Quadratics",
    "Factoring General Quadratics",
    "Sum and Product of Roots",
    "Square of a Binomial",
    "Difference-of-Squares",
    "Rationalizing Denominators",
    "Simon's Favorite Factoring Trick",
    "Quadratic Formula/Discriminant",
    "Completing the Square",
    "Quadratic Optimization",
    "Graphing Quadratics",
    "Quadratic Inequalities",
    "Domain and Range",
    "Function Composition",
    "Inverse Functions",
    "Functional Operations",
    "Graphing Functions",
    "Exponential and Logarithm Basics",
    "Interest Rates",
    "Logarithm Basics",
    "Radical Expressions and Functions",
    "Absolute Value",
    "Floor and Ceiling",
    "Rational Expressions of Polynomials",
    "Piecewise-Defined Functions",
    "Arithmetic Sequences",
    "Arithmetic Series",
    "Geometric Sequences",
    "Geometric Series",
    "Clever Algebraic Manipulations",

    # Number Theory
    "Multiples",
    "Divisors",
    "Primes and Composites",
    "Remainders",
    "Prime Factorization",
    "Least Common Multiple",
    "Greatest Common Divisor",
    "The Euclidean Algorithm",
    "LCM/GCD Problem-Solving",
    "Counting Divisors",
    "Divisor Arithmetic",
    "Converting from Base 10",
    "Converting to Base 10",
    "Base Number Problem-Solving",
    "Base Number Arithmetic",
    "The Last Digit (Base 10)",
    "Terminating Decimals",
    "Repeating Decimals",
    "Congruence and Residues",
    "Modular Arithmetic Sums",
    "Patterns in Modular Arithmetic",
    "Divisibility Rules",
    "Divisibility Problem-Solving",
    "Modular Arithmetic Inverses",
    "Modular Arithmetic Congruences",
    "Modular Arithmetic Systems",
    "Perfect Powers",
    "Digits",

    # Counting and Probability
    "Counting Numbers in Lists",
    "Venn Diagrams",
    "Counting Independent Events",
    "Factorials",
    "Permutations",
    "Casework Counting",
    "Complementary Counting",
    "Constructive Counting",
    "Counting with Restrictions",
    "Counting with Symmetry",
    "Correcting for Overcounting with Division",
    "Combinations",
    "Computing Combinations",
    "Combinations with Restrictions",
    "Distinguishability",
    "Probability as Counting",
    "Probability with Combinations",
    "Probability with Casework",
    "Complementary Probability",
    "Binomial Probability",
    "Multiplying Probabilities",
    "Probability - Think About It!",
    "Using Geometry in Probability",
    "Expected Value",
    "Pascal's Triangle",
    "Binomial Theorem",

    # Geometry
    "Angle Measurement",
    "Angles, Parallel Lines, and Triangles",
    "Isosceles and Equilateral Triangles",
    "Length and Perimeter",
    "Area",
    "Similar Triangles",
    "The Pythagorean Theorem",
    "Special Right Triangles",
    "Bisectors in a Triangle",
    "Triangle Medians and Altitudes",
    "Quadrilaterals",
    "Polygon Angles",
    "Polygon Length and Area",
    "Inequalities in Triangles",
    "Circle Area and Circumference",
    "Funky Circle Areas",
    "Angles in Circles",
    "Lengths in Circles",
    "Prisms",
    "Pyramids",
    "Cylinders",
    "Cones",
    "Spheres",
    "Transformations",
    "Analytic Geometry",
    "Right-Triangle Trigonometry",
    "Unit Circle Trigonometry",

    # Intermediate Algebra
    "Complex Number Arithmetic",
    "Magnitude of Complex Numbers",
    "Complex Numbers",
    "Quadratic Inequalities",
    "Graphing Quadratics",
    "Quadratic Formula/Discriminant",
    "Sum and Product of Roots",
    "Quadratic Optimization",
    "Circles",
    "Ellipses",
    "Hyperbolas",
    "Parabolas",
    "Conic Sections",
    "Polynomial Division Algorithms",
    "Remainder and Factor Theorem",
    "Polynomial Forms",
    "Integer/Rational Roots",
    "Irrational Roots",
    "Complex Roots",
    "Polynomial Interpolation",
    "Vieta's Formulas",
    "Polynomial Roots",
    "Sequences and Series",
    "Telescoping Series",
    "General Sequences and Series",
    "Recursively Defined Sequences",
    "Exponents and Logarithms",
    "Radicals",
    "Even and Odd Functions",
    "Graphs of Rational Functions",
    "Rational Function Equations and Inequalities",
    "Partial Fractions",
    "Inequality Skills",
    "AM-GM Inequality",
    "Cauchy-Schwarz Inequality",
    "Power Mean Inequality",
    "Inequalities",
    "Factorization Identities",
    "Functional Equations",
    "Systems of Equations",
    "Binomial Theorem",

    # Pre-Calculus
    "Graphs of Trigonometric Functions",
    "Inverse Trigonometric Functions",
    "Trigonometric Identities",
    "Sums and Differences of Angles",
    "Double and Half Angle Identities",
    "Sum-to-Product and Product-to-Sum",
    "Solving Trigonometric Equations",
    "Triangle Geometry",
    "Parametric Curves",
    "Polar Coordinates",
    "3D Coordinates",
    "Spherical and Cylindrical Coordinates",
    "The Complex Plane",
    "Polar Form of Complex Numbers",
    "Exponential Form of Complex Numbers",
    "Roots of Unity",
    "Geometry of Complex Numbers",
    "2D Vector Basics",
    "Lines with 2D Vectors",
    "Projections of 2D Vectors",
    "Solving Geometry Problems with Vectors",
    "2D Matrix Basics",
    "2D Matrix Transformations",
    "2D Matrix Determinant",
    "2D Matrix Inverses",
    "3D Vector Basics",
    "Lines with 3D Vectors",
    "Cross Product",
    "Planes with 3D Vectors",
    "Projections of 3D Vectors",
    "3D Matrix Basics",
    "3D Matrix Determinant"
]

import sys
from random import choice

if len(sys.argv) == 2:
    # Prints out [second command-line arguement - the one after main.py] number of vectors
    for i in range(sys.argv[1]):
        print(choice(list_of_math_topics))
else:
    print("Please list the number of math topics you want as the command-line arguement after main.py.\nRead README.md for more information.")