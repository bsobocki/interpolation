# A program to image playback by interpolating polynomials
Simple program which uses interpolation to image playback

# Description

Reads an PNG file, finds pixels that aren’t white, based on selected ones interpolates functions responsible for the X and Y coordinates ( S<sub>x</sub>(t) and S<sub>y</sub>(t) ) and creates a plot (parametric curve) imitating the image.

# Interpolation

K-th interpolating polynomial is expressed by the formula:  

S<sub><sub>k</sub></sub>(x) = h<sub><sub>k</sub></sub><sup>-1</sup>  \[   <sup>1</sup>/<sub>6</sub> M<sub><sub>k-1</sub></sub> \(x<sub><sub>k</sub></sub> - x)<sup>3</sup>  +  <sup>1</sup>/<sub>6</sub> M<sub><sub>k</sub></sub> \(x - x<sub><sub>k-1</sub></sub>)<sup>3</sup>  + \(y<sub><sub>k-1</sub></sub> - <sup>1</sup>/<sub>6</sub> M<sub><sub>k-1</sub></sub> h<sub><sub>k</sub></sub><sup>2</sup>)\(x<sub><sub>k</sub></sub> - x) + \(y<sub><sub>k</sub></sub> - <sup>1</sup>/<sub>6</sub> M<sub><sub>k</sub></sub> h<sub><sub>k</sub></sub><sup>2</sup>)\(x - x<sub><sub>k-1</sub></sub>) ]
 
