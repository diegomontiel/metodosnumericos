{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "import math\n",
    "\n",
    "x = [200,400,500,700,900,1000]\n",
    "y = [60,120,150,210,260,290]\n",
    "n = 6\n",
    "plt.plot(x, y, 'ro')\n",
    "plt.show()\n",
    "\n",
    "sumx = sum(x)\n",
    "sumy = sum(y)\n",
    "sumx2 = sum( xi * xi for xi in x  )\n",
    "sumxy = sum ( xi * yi for xi, yi in zip(x,y) )\n",
    "\n",
    "m = (sumxy - (sumx*sumy/n))/(sumx2 - (sumx*sumx/n))\n",
    "b = (sumy/n) - (m * (sumx/n))\n",
    "\n",
    "print(m,b)\n",
    "\n",
    "# Ejemplo 2 regresion con parabola\n",
    "x = [0.001,1,2,3,4,5]\n",
    "y = [2.1,7.7,13.6,27.2,40.9,61.1]\n",
    "n = 6\n",
    "plt.plot(x, y, 'ro')\n",
    "plt.show()\n",
    "logx = [math.log10(xi) for xi in x]\n",
    "logy = [math.log10(yi) for yi in y]\n",
    "x = logx\n",
    "y = logy\n",
    "\n",
    "sumx = sum(x)\n",
    "sumy = sum(y)\n",
    "sumx2 = sum( xi * xi for xi in x  )\n",
    "sumxy = sum ( xi * yi for xi, yi in zip(x,y) )\n",
    "\n",
    "m = (sumxy - (sumx*sumy/n))/(sumx2 - (sumx*sumx/n))\n",
    "b = (sumy/n) - (m * (sumx/n))\n",
    "alpha = 10**b\n",
    "beta = m\n",
    "\n",
    "print (\"alpha, beta\",alpha,beta)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "SageMath (stable)",
   "language": "sagemath",
   "name": "sagemath"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.15"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}