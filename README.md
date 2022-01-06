# MA2151-Simulation-and-Mathematical-Computation
All project done for MA2151 - Simulation and Mathematical Computation subject in the 3rd semester at Bandung Institute of Technology 

## 1. Average and Gaussian Blur
### Library Used : Pillow and Numpy 
an image processing script that takes image as the input and output processed image by blurring the image with Average or Gaussian method by manipulating the RGB matriks of the image, 
### Preview : 
#### Input : 

<img src="https://github.com/FelixFern/MA2151-Simulation-and-Mathematical-Computation/blob/main/Average%20Blur%20and%20Gaussian%20Blur/input-image.png?raw=true" alt="input" width="20%" align="center"/>

#### Output : 

Gaussian Blur : 

<img src="https://github.com/FelixFern/MA2151-Simulation-and-Mathematical-Computation/blob/main/Average%20Blur%20and%20Gaussian%20Blur/output-image-gaussian.png?raw=true" alt="input" width="20%" align="center"/>

Average Blur : 

<img src="https://github.com/FelixFern/MA2151-Simulation-and-Mathematical-Computation/blob/main/Average%20Blur%20and%20Gaussian%20Blur/output-image-average.png?raw=true" alt="input" width="20%" align="center"/>


## 2. Pit Viper Simulation
### Library Used : Numpy and Matplotlib 
a simulation of pit viper hunting for prey (rodent) with the following rules : 
- Viper and Rodent is placed in a closed environment in form of a N x N sized grid
- This simulation used the reflecting boundary condition for the heat grid and the absorbing boundary condition for the main grid
- Viper and Rodent move by using the moore neighbourhood which consist of 8 different direction (N, NE, S, SW, W, SE, E, NW)
- Viper has the ability to detect heat differences and walk toward the highest temperature 
- Rodent have body temperature of 37 degree celcius with 0 degree celcius for the environment temperature
- Rodent walk randomly in the closed environment
- Rodent temperature affect the surrounding environment temperature 

### Preview : 

<img src="https://github.com/FelixFern/MA2151-Simulation-and-Mathematical-Computation/blob/main/Pit%20Viper%20Simulation/pit-viper-simulation.gif?raw=true" alt="input" width="50%" align="center"/>
