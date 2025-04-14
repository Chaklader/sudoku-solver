# C-7 | S-3: Logical Agents and Propositional Logic

1. Knowledge-Based Agents
    - The Knowledge-Based Agent Architecture
    - TELL and ASK Interface
    - The Wumpus World Environment as a Test Case
    - Knowledge Engineering for Agent Design
2. Propositional Logic Fundamentals
    - Syntax and Semantics of Propositional Logic
    - Truth Tables and Logical Connectives
    - Equivalence, Validity, and Satisfiability
    - Entailment and Logical Consequence
3. Inference in Propositional Logic
    - Model Checking and Truth Tables
    - Proof-Based Inference Methods
    - The Resolution Rule and Resolution Proofs
    - Completeness of Resolution
4. Efficient Propositional Inference
    - The DPLL Algorithm
    - Heuristics for SAT Solving
    - Local Search for Satisfiability
    - The Threshold Phenomenon in Random SAT

# C-8 | S-3: First-Order Logic

1. Beyond Propositional Logic
    - Limitations of Propositional Representations
    - Syntax and Semantics of First-Order Logic
    - Terms, Predicates, and Quantifiers
    - Models for First-Order Logic
2. Representing Knowledge in First-Order Logic
    - Assertions and Queries in First-Order Logic
    - The Kinship Domain Example
    - Numbers, Sets, and Lists
    - The Wumpus World in First-Order Logic
3. Equality and Functions in FOL
    - Identity and Substitution
    - Functions and Functional Terms
    - Extending FOL with Equality
    - Unique Names and Domain Closure
4. Knowledge Engineering in First-Order Logic
    - The Process of Knowledge Engineering
    - Representing the Electronic Circuits Domain
    - Organizing Knowledge with Classes and Instances
    - Testing and Debugging Knowledge Bases

# C-9 | S-3: Inference in First-Order Logic

1. Propositional vs. First-Order Inference
    - Universal and Existential Instantiation
    - Reduction to Propositional Inference
    - Herbrand's Theorem
    - Semidecidability of First-Order Logic
2. Unification and Lifting
    - The Unification Algorithm
    - Most General Unifiers
    - Efficient Storage and Retrieval of Facts
    - Lifting Propositional Inference Rules
3. Forward and Backward Chaining
    - First-Order Definite Clauses
    - Forward Chaining Algorithms and Optimizations
    - Backward Chaining and Goal-Directed Inference
    - Logic Programming with Prolog
4. Resolution-Based Theorem Proving
    - Conjunctive Normal Form for First-Order Logic
    - First-Order Resolution
    - Strategies for Resolution-Based Inference
    - Handling Equality in Resolution

# C-10 | S-3: Knowledge Representation

1. Ontological Engineering
    - Upper Ontologies and Knowledge Organization
    - Categories and Objects
    - Physical Composition and Measurements
    - Distinguishing Things and Stuff
2. Events and Time
    - The Event Calculus
    - Interval Algebra and Temporal Relations
    - Fluents and Objects
    - Representing Actions and Their Effects
3. Mental Objects and Modal Logic
    - Representing Knowledge About Knowledge
    - Modal Operators for Knowledge and Belief
    - Reasoning About Knowledge and Belief
    - Limitations of Logical Omniscience
4. Reasoning Systems for Categories
    - Semantic Networks
    - Description Logics
    - Default Reasoning
    - Truth Maintenance Systems

# C-7 | S-4: Quantifying Uncertainty

1. Acting under Uncertainty
    - Sources of Uncertainty in AI Systems
    - Logical vs. Probabilistic Approaches
    - The Qualification Problem
    - Decision Making Under Uncertainty
2. Basic Probability Notation
    - Sample Spaces and Events
    - Prior and Conditional Probabilities
    - Random Variables and Distributions
    - The Chain Rule and Marginalization
3. Inference Using Full Joint Distributions
    - Computing Posterior Probabilities
    - Summing Out Variables
    - Normalization Techniques
    - Computational Complexity of Joint Inference
4. Independence
    - Absolute Independence Between Variables
    - Factoring the Joint Distribution
    - Compactness Through Independence
    - Independence Assertions in Real-World Domains
5. Bayes' Rule and Its Use
    - Diagnostic and Causal Reasoning
    - Applying Bayes' Rule with Multiple Pieces of Evidence
    - Naive Bayes Models
    - Text Classification with Naive Bayes
6. The Wumpus World Revisited
    - Probabilistic Reasoning in the Wumpus World
    - Computing Posterior Probabilities for Pits
    - Using Independence in Wumpus Inference
    - Performance of Probabilistic vs. Logical Agents

# C-8 | S-4: Probabilistic Reasoning

1. Representing Knowledge in an Uncertain Domain
    - Limitations of Propositional Approaches
    - Bayesian Networks as Knowledge Representation
    - Nodes, Arcs, and Conditional Probability Tables
    - Constructing Bayesian Networks from Causal Knowledge
2. The Semantics of Bayesian Networks
    - Representing the Full Joint Distribution
    - Conditional Independence in Bayesian Networks
    - D-Separation and Markov Blankets
    - Compact Representations of Conditional Distributions
3. Exact Inference in Bayesian Networks
    - Variable Elimination Algorithm
    - Factors and Factor Operations
    - Complexity of Exact Inference
    - Clustering Algorithms and Junction Trees
4. Approximate Inference for Bayesian Networks
    - Direct Sampling Methods
    - Rejection Sampling
    - Likelihood Weighting
    - Markov Chain Monte Carlo Methods
5. Causal Networks
    - Representing Actions with the Do-Operator
    - Interventions vs. Observations
    - The Back-Door Criterion
    - Counterfactual Reasoning

# C-9 | S-4: Probabilistic Reasoning over Time

1. Time and Uncertainty
    - States and Observations
    - Transition and Sensor Models
    - Markov Assumptions
    - Stationarity and Time Homogeneity
2. Inference in Temporal Models
    - Filtering and Prediction
    - Smoothing
    - Finding the Most Likely Sequence
    - The Forward-Backward Algorithm
3. Hidden Markov Models
    - Definition and Structure
    - Matrix Implementation of HMM Algorithms
    - The Viterbi Algorithm
    - Applications of HMMs to Localization
4. Kalman Filters
    - Linear Dynamical Systems
    - Gaussian Distributions and Updates
    - Prediction and Correction Steps
    - Extended Kalman Filters for Nonlinear Systems
5. Dynamic Bayesian Networks
    - DBNs as Generalizations of HMMs and Kalman Filters
    - Constructing DBNs
    - Exact Inference in DBNs
    - Particle Filtering and Sequential Importance Sampling

# C-10 | S-4: Making Simple Decisions

1. Combining Beliefs and Desires Under Uncertainty
    - Utility Theory Basics
    - Preference Orderings
    - Axioms of Utility Theory
    - Maximum Expected Utility Principle
2. Utility Functions
    - Properties of Utility Functions
    - Risk Aversion and Risk Seeking
    - The Utility of Money
    - Multiattribute Utility Functions
3. Decision Networks
    - Representing Decision Problems
    - Influence Diagrams
    - Computing the Value of Perfect Information
    - Sequential Decision Problems
4. The Value of Information
    - Definition and Properties
    - Computing Value of Information
    - Applications to Expert Systems
    - Information Gathering Agents

# C-11 | S-4: Probabilistic Programming

1. Properties of Multiagent Environments
    - Agents vs. Counterparts
    - Benevolent Agent Assumption
    - Cooperative vs. Non-cooperative Settings
    - Strategic vs. Coordinated Decision Making
    - Information Sharing and Communication Protocols
2. Relational Probability Models
    - Syntax and Semantics of RPMs
    - Basic Random Variables
    - Dependency Statements and Context-Specific Independence
    - Example: Rating Player Skill Levels
    - Inference in Relational Probability Models
3. Open-Universe Probability Models
    - Syntax and Semantics of OUPMs
    - Existence and Identity Uncertainty
    - Number Statements and Origin Functions
    - Examples: Citation Matching and Treaty Monitoring
    - Algorithms for OUPM Inference
4. Keeping Track of a Complex World
    - Multitarget Tracking Problem
    - Data Association and Identity Uncertainty
    - Tracking with False Alarms and Detection Failures
    - Example: Traffic Monitoring
    - Computational Approaches to Identity Management
5. Programs as Probability Models
    - Generative Programs and Execution Traces
    - Example: Reading Degraded Text
    - Syntax and Semantics of Probabilistic Programs
    - Improving Models with Markov Processes
    - Inference in Generative Programs

# C-12 | S-4: Making Complex Decisions

1. Sequential Decision Problems
    - Markov Decision Processes (MDPs)
    - Transition Models and Reward Functions
    - Utilities over Time and Discount Factors
    - Optimal Policies and State Utilities
    - Representing MDPs with Dynamic Decision Networks
2. Algorithms for MDPs
    - Value Iteration
    - Policy Iteration
    - Linear Programming Approaches
    - Online Algorithms for MDPs
    - Monte Carlo Tree Search for MDPs
3. Bandit Problems
    - The n-Armed Bandit Setting
    - The Bernoulli Bandit
    - Computing the Gittins Index
    - Exploration vs. Exploitation
    - Approximately Optimal Bandit Policies
4. Partially Observable MDPs
    - Definition of POMDPs
    - Belief States and Updates
    - Converting POMDPs to Belief-State MDPs
    - The Value of Information in POMDPs
    - Applications of POMDPs
5. Algorithms for Solving POMDPs
    - Value Iteration for POMDPs
    - Policy Loss and Convergence
    - Online Algorithms for POMDPs
    - Monte Carlo Planning for POMDPs
    - Partially Observable Monte Carlo Planning (POMCP)

# C-13 | S-4: Multiagent Decision Making

1. Properties of Multiagent Environments
    - One Decision Maker vs. Multiple Decision Makers
    - Coordination Problems and Common Goals
    - Multieffector Planning and Multibody Planning
    - Decentralized and Distributed Planning
    - Incentive Alignment in Multiagent Systems
2. Non-Cooperative Game Theory
    - Games with a Single Move: Normal Form Games
    - Dominant Strategies and Nash Equilibrium
    - Social Welfare and Pareto Optimality
    - Computing Equilibria
    - Repeated Games and Sequential Games
3. Cooperative Game Theory
    - Coalition Structures and Outcomes
    - The Core and Shapley Value
    - Stability and Fairness Concepts
    - Computation in Cooperative Games
    - Marginal Contribution Networks
4. Making Collective Decisions
    - Allocating Tasks with the Contract Net
    - Auctions for Resource Allocation
    - Voting Systems and Social Choice
    - Bargaining and Negotiation
    - Mechanism Design for Multiagent Systems
5. Uncertain Payoffs and Assistance Games
    - Preference Uncertainty in Games
    - Assistance Games and Human-AI Alignment
    - The Paperclip Game
    - Deference to Humans
    - Computing Equilibria with Uncertain Preferences

# C-14 | S-4: Probabilistic Reasoning Systems

1. Knowledge Engineering for Bayesian Networks
    - Identifying Variables and Values
    - Determining Network Structure
    - Eliciting Probabilities
    - Sensitivity Analysis
    - Knowledge Engineering Tools
2. Temporal Reasoning Systems
    - Dynamic Probabilistic Models
    - Reasoning with Time and Uncertainty
    - Filtering and Prediction Algorithms
    - Applications in Robotics and Finance
    - Hybrid Approaches for Complex Domains
3. Decision Support Systems
    - Medical Diagnosis Systems
    - Financial Decision Support
    - Environmental Monitoring
    - Explainable Recommendations
    - Risk Assessment and Management
4. Inference Systems at Scale
    - Distributed Inference Algorithms
    - Approximate Methods for Large Networks
    - Real-time Inference Systems
    - Combining Logical and Probabilistic Reasoning
    - Applications in Large-Scale Monitoring
5. Learning in Probabilistic Systems
    - Parameter Estimation from Data
    - Structure Learning Algorithms
    - Transfer Learning in Probabilistic Models
    - Online Learning in Dynamic Environments
    - Evaluation of Learned Probabilistic Systems

# C-15 | S-4: Advanced Topics in Uncertainty

1. Decision Theory and Ethics
    - Fairness in Decision Making
    - Handling Value Uncertainty
    - Ethical Considerations in Utility Design
    - Group Decision Making
    - Accountability in Automated Decisions
2. Computational Complexity of Reasoning
    - Tractable and Intractable Inference Problems
    - Hardness Results for Probabilistic Inference
    - Complexity Classes for Decision Problems
    - Approximation Guarantees
    - Practical Performance vs. Theoretical Bounds
3. Multi-agent Reasoning under Uncertainty
    - Distributed Belief Updates
    - Reasoning about Other Agents' Beliefs
    - Strategic Information Revelation
    - Collaborative Filtering and Decision Making
    - Applications in Autonomous Systems
4. Non-standard Models of Uncertainty
    - Dempster-Shafer Theory
    - Possibility Theory
    - Imprecise Probabilities
    - Quantum Probabilities
    - Applications of Alternative Uncertainty Models
5. Cognitive Models of Reasoning
    - Human Reasoning Under Uncertainty
    - Biases and Heuristics
    - Psychological Models of Decision Making
    - Computational Models of Human Judgment
    - Implications for AI System Design

# C-16 | S-5: Learning from Examples

1. Forms of Learning
    - Components That Can Be Improved Through Learning
    - Inductive Learning from Examples
    - Supervised vs. Unsupervised Learning
    - Classification vs. Regression Problems
    - Online vs. Batch Learning
2. Supervised Learning
    - The Learning Problem
    - Hypothesis Spaces and Inductive Bias
    - Generalization and Overfitting
    - Evaluating Learning Algorithms with Cross-Validation
3. Learning Decision Trees
    - Decision Tree Representation
    - Expressiveness of Decision Trees
    - Learning Decision Trees from Examples
    - Choosing Attribute Tests with Information Gain
    - Generalization and Overfitting in Decision Trees
    - Pruning to Avoid Overfitting
    - Broadening the Applicability of Decision Trees
4. Model Selection and Optimization
    - Model Selection Algorithms
    - From Error Rates to Loss
    - Regularization
    - Hyperparameter Tuning
5. The Theory of Learning
    - PAC Learning
    - Sample Complexity and Learning Decision Lists
    - Computational Complexity of Learning
6. Linear Regression and Classification
    - Univariate Linear Regression
    - Gradient Descent
    - Multivariable Linear Regression
    - Linear Classifiers with a Hard Threshold
    - Linear Classification with Logistic Regression
7. Nonparametric Models
    - Nearest-Neighbor Models
    - Finding Nearest Neighbors with k-d Trees
    - Locality-Sensitive Hashing
    - Nonparametric Regression
    - Support Vector Machines
8. Ensemble Learning
    - Bagging
    - Random Forests
    - Stacking
    - Boosting
    - Gradient Boosting
    - Online Learning
9. Developing Machine Learning Systems
    - Problem Formulation
    - Data Collection, Assessment, and Management
    - Model Selection and Training
    - Trust, Interpretability, and Explainability
    - Operation, Monitoring, and Maintenance

# C-17 | S-5: Probabilistic Machine Learning

1. Statistical Learning
    - Bayesian Learning as Probabilistic Inference
    - Maximum a Posteriori (MAP) Learning
    - Maximum-Likelihood Learning
    - Probabilistic and Non-Probabilistic Approaches
2. Learning with Complete Data
    - Maximum-Likelihood Parameter Learning for Discrete Models
    - Naive Bayes Models
    - Generative and Discriminative Models
    - Maximum-Likelihood Parameter Learning for Continuous Models
    - Bayesian Parameter Learning
    - Bayesian Linear Regression
    - Learning Bayes Net Structures
    - Density Estimation with Nonparametric Models
3. Learning with Hidden Variables: The EM Algorithm
    - Unsupervised Clustering: Learning Mixtures of Gaussians
    - Learning Bayes Net Parameter Values for Hidden Variables
    - Learning Hidden Markov Models
    - The General Form of the EM Algorithm
    - Learning Bayes Net Structures with Hidden Variables

# C-18 | S-5: Deep Learning

1. Simple Feedforward Networks
    - Networks as Complex Functions
    - Gradients and Learning
2. Computation Graphs for Deep Learning
    - Input Encoding
    - Output Layers and Loss Functions
    - Hidden Layers
3. Convolutional Networks
    - Kernels and Convolution Operations
    - Pooling and Downsampling
    - Tensor Operations in CNNs
    - Residual Networks
4. Learning Algorithms
    - Computing Gradients in Computation Graphs
    - Batch Normalization
5. Generalization
    - Choosing a Network Architecture
    - Neural Architecture Search
    - Weight Decay
    - Dropout
6. Recurrent Neural Networks
    - Training a Basic RNN
    - Long Short-Term Memory RNNs
7. Unsupervised Learning and Transfer Learning
    - Unsupervised Learning
        - Probabilistic PCA
        - Autoencoders
        - Variational Autoencoders
        - Deep Autoregressive Models
        - Generative Adversarial Networks
        - Unsupervised Translation
    - Transfer Learning and Multitask Learning
8. Applications
    - Vision
    - Natural Language Processing
    - Reinforcement Learning

# C-19 | S-5: Reinforcement Learning

1. Learning from Rewards
    - Reinforcement Learning vs. Supervised Learning
    - Types of Reinforcement Learning Approaches
        - Model-Based Methods
        - Model-Free Methods (Action-Utility Learning, Policy Search)
2. Passive Reinforcement Learning
    - Direct Utility Estimation
    - Adaptive Dynamic Programming
    - Temporal-Difference Learning
3. Active Reinforcement Learning
    - Exploration
        - Greedy vs. Exploratory Approaches
        - Exploration Functions
    - Safe Exploration
    - Temporal-Difference Q-Learning
        - Q-Learning vs. SARSA
4. Generalization in Reinforcement Learning
    - Approximating Direct Utility Estimation
    - Approximating Temporal-Difference Learning
    - Deep Reinforcement Learning
    - Reward Shaping
    - Hierarchical Reinforcement Learning
        - Joint State Space and Choice States
        - Partial Programs
5. Policy Search
    - Policy Value and Policy Gradient
    - Stochastic Policies
    - Correlated Sampling
6. Apprenticeship and Inverse Reinforcement Learning
    - Imitation Learning
    - Inverse Reinforcement Learning
    - Feature Matching and Feature Expectations
    - Boltzmann Rationality
7. Applications of Reinforcement Learning
    - Applications in Game Playing
        - Backgammon (TD-Gammon)
        - Atari Games (DQN)
        - Go (AlphaGo)
    - Application to Robot Control
        - Cart-Pole Balancing
        - Helicopter Flight

# C-20 | S-6: Natural Language Processing

1. Language Models
    - The Bag-of-Words Model
    - N-gram Word Models
    - Other N-gram Models
    - Smoothing N-gram Models
    - Word Representations
    - Part-of-Speech (POS) Tagging
    - Comparing Language Models
2. Grammar
    - The Lexicon of E₀
    - Formal Grammars and Language Definitions
    - Syntactic Categories and Phrase Structure
3. Parsing
    - Top-Down vs. Bottom-Up Parsing
    - Chart Parsing and the CYK Algorithm
    - Chomsky Normal Form
    - Dependency Parsing
    - Learning a Parser from Examples
4. Augmented Grammars
    - Agreement Features and Subcategories
    - Semantic Interpretation
    - Learning Semantic Grammars
5. Complications of Real Natural Language
    - Quantification
    - Pragmatics and Indexicals
    - Long-Distance Dependencies
    - Time and Tense
    - Ambiguity (Lexical, Syntactic, Semantic)
    - Metaphor and Metonymy
    - Disambiguation Methods
6. Natural Language Tasks
    - Speech Recognition and Text-to-Speech
    - Machine Translation
    - Information Extraction
    - Information Retrieval
    - Question Answering

# C-21 | S-6: Deep Learning for Natural Language Processing

1. Word Embeddings
    - From One-Hot Vectors to Continuous Representations
    - Properties of Word Embedding Spaces
    - Applications of Word Embeddings
2. Recurrent Neural Networks for NLP
    - Language Models with RNNs
    - Classification with RNNs
    - LSTMs for NLP Tasks
    - Bidirectional RNNs
3. Sequence-to-Sequence Models
    - Basic Structure and Limitations
    - Attention Mechanisms
    - Decoding Methods (Greedy vs. Beam Search)
    - Applications in Machine Translation
4. The Transformer Architecture
    - Self-Attention
    - Positional Encoding
    - Transformer Encoder-Decoder Structure
5. Pretraining and Transfer Learning
    - Pretrained Word Embeddings
    - Pretrained Contextual Representations
    - Masked Language Models
    - Fine-Tuning for Specific Tasks
6. State of the Art
    - Language Models (GPT, T5)
    - Question Answering and Reading Comprehension
    - Limitations and Future Directions

# C-22 | S-6: Computer Vision

1. Image Formation
    - Pinhole Camera Model
    - Perspective Projection
    - Lens Systems
    - Scaled Orthographic Projection
    - Light and Shading
    - Color and Trichromacy
2. Simple Image Features
    - Edges and Edge Detection
    - Texture Representation
    - Optical Flow
    - Segmentation of Natural Images
3. Classifying Images
    - Appearance Variation Challenges
    - Convolutional Neural Networks for Classification
    - Feature Learning and Transfer
    - Data Augmentation Techniques
4. Detecting Objects
    - Bounding Box Representation
    - Regional Proposal Networks
    - Non-Maximum Suppression
    - Bounding Box Regression
5. The 3D World
    - 3D Cues from Multiple Views
    - Binocular Stereopsis
    - 3D Cues from Moving Cameras
    - 3D Cues from a Single View
6. Using Computer Vision
    - Human Action Understanding
    - Linking Pictures and Words (Captioning, VQA)
    - Reconstruction from Multiple Views
    - Geometry from a Single View
    - Image Generation and Transformation
    - Vision for Movement Control

# C-23 | S-6: Robotics

1. Robot Hardware
    - Types of Robots (Manipulators, Mobile, Legged)
    - Sensing the World (Active/Passive Sensors)
    - Effectors and Motion Production
2. Problem Formulation in Robotics
    - Computational Frameworks (MDPs, POMDPs, Games)
    - Hierarchical Planning Decomposition
    - Preference Learning and People Prediction
3. Robotic Perception
    - State Estimation and Filtering
    - Localization and Mapping
    - SLAM and Other Perception Types
    - Machine Learning in Perception
4. Planning and Control
    - Configuration Space
    - Motion Planning Algorithms
    - Trajectory Tracking Control
    - Optimal Control Approaches
5. Planning Uncertain Movements
    - Online Replanning
    - Model Predictive Control
    - Information Gathering Actions
    - Guarded Movements
6. Reinforcement Learning in Robotics
    - Exploiting Models
    - Sim-to-Real Transfer
    - Domain Randomization
    - Sample Efficiency Techniques
7. Humans and Robots
    - Coordination Challenges
    - Game Theory Approaches
    - Predicting Human Actions
    - Learning Human Preferences
    - Imitation Learning
8. Alternative Robotic Frameworks
    - Reactive Controllers
    - Subsumption Architecture
    - Limitations of Different Approaches
9. Application Domains
    - Home Care and Assistance
    - Healthcare and Surgery
    - Service Robots and Delivery
    - Autonomous Vehicles
    - Entertainment and Animatronics
    - Exploration and Hazardous Environments
    - Industrial Automation
