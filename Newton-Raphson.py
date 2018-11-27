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
    "def createMatrix(m,n,v):\n",
    "    C = []\n",
    "    for i in range(m):\n",
    "        C.append([v]*n)\n",
    "    return C\n",
    "\n",
    "def getDimensions(A):\n",
    "    return (len(A),len(A[0]))\n",
    "\n",
    "def copyMatrix(B):\n",
    "    m,n = getDimensions(B)\n",
    "    A = createMatrix(m,n,0)\n",
    "    for i in range(m):\n",
    "        for j in range(n):\n",
    "            A[i][j] = B[i][j]\n",
    "    return A\n",
    "\n",
    "def sumaMatrix(A,B):\n",
    "    Am,An = getDimensions(A)\n",
    "    Bm,Bn = getDimensions(B)\n",
    "    if Am != Bm or An != Bn:\n",
    "        print(\"Error las dimensiones deben ser iguales\")\n",
    "        return []\n",
    "    C = createMatrix(Am,An,0)\n",
    "    for i in range(Am):\n",
    "        for j in range(An):\n",
    "            C[i][j] = A[i][j] + B[i][j]\n",
    "    return C\n",
    "\n",
    "def restaMatrix(A,B):\n",
    "    Am,An = getDimensions(A)\n",
    "    Bm,Bn = getDimensions(B)\n",
    "    if Am != Bm or An != Bn:\n",
    "        print(\"Error las dimensiones deben ser iguales\")\n",
    "        return []\n",
    "    C = createMatrix(Am,An,0)\n",
    "    for i in range(Am):\n",
    "        for j in range(An):\n",
    "            C[i][j] = A[i][j] - B[i][j]\n",
    "    return C\n",
    "\n",
    "def multMatrix(A,B):\n",
    "    Am,An = getDimensions(A)\n",
    "    Bm,Bn = getDimensions(B)\n",
    "    if An != Bm:\n",
    "        print(\"Error las dimensiones deben ser conformable\")\n",
    "        return []\n",
    "    C = createMatrix(Am,Bn,0)\n",
    "    for i in range(Am):\n",
    "        for j in range(Bn):\n",
    "            for k in range(An):\n",
    "                    C[i][j] += A[i][k] * B[k][j]\n",
    "    return C\n",
    "    \n",
    "def getAdyacente(A,r,c):\n",
    "    Am,An = getDimensions(A)\n",
    "    C = createMatrix(Am-1,An-1,0)\n",
    "    for i in range(Am):\n",
    "        if i == r:\n",
    "            continue\n",
    "        for j in range(An):\n",
    "            if j == c:\n",
    "                continue\n",
    "            ci = 0\n",
    "            cj = 0\n",
    "            if(i < r):\n",
    "                ci = i\n",
    "            else:\n",
    "                ci = i - 1\n",
    "            if(j < c):\n",
    "                cj = j\n",
    "            else:\n",
    "                cj = j - 1\n",
    "            C[ci][cj] = A[i][j]\n",
    "    return C\n",
    "\n",
    "def detMatrix(A):\n",
    "    m,n = getDimensions(A)\n",
    "    if m != n:\n",
    "        print(\"La matriz no es cuadrada\")\n",
    "        return []\n",
    "    if m == 1:\n",
    "        return A[0][0]\n",
    "    if m == 2:\n",
    "        return A[0][0]*A[1][1] - A[1][0]*A[0][1]\n",
    "    det = 0\n",
    "    for j in range(m):\n",
    "        det += ((-1)**j)*A[0][j]*detMatrix(getAdyacente(A,0,j))\n",
    "    return det\n",
    "\n",
    "\n",
    "def getMatrizTranspuesta(A):\n",
    "    m,n = getDimensions(A)\n",
    "    C = createMatrix(n,m,0)\n",
    "    for i in range(m):\n",
    "        for j in range(n):\n",
    "            C[j][i] = A[i][j]\n",
    "    return C\n",
    "\n",
    "def getMatrizAdjunta(A):\n",
    "    m,n = getDimensions(A)\n",
    "    if m != n:\n",
    "        print(\"La matriz no es cuadrada\")\n",
    "        return []\n",
    "    C = createMatrix(m,n,0)\n",
    "    for i in range(m):\n",
    "        for j in range(n):\n",
    "            C[i][j] = ((-1)**(i+j))*detMatrix(getAdyacente(A,i,j))\n",
    "    return C\n",
    "\n",
    "def getMatrizInversa(A):\n",
    "    m,n = getDimensions(A)\n",
    "    if m != n:\n",
    "        print(\"La matriz no es cuadrada\")\n",
    "        return []\n",
    "    detA = detMatrix(A)\n",
    "    if detA == 0:\n",
    "        print(\"La matriz no tiene inversa\")\n",
    "        return []\n",
    "    At = getMatrizTranspuesta(A)\n",
    "    adjA = getMatrizAdjunta(At)\n",
    "    invDetA = 1/detA\n",
    "    C = createMatrix(m,n,0)\n",
    "    for i in range(m):\n",
    "        for j in range(n):\n",
    "            C[i][j] = invDetA * adjA[i][j]\n",
    "    return C\n",
    "##########\n",
    "\n",
    "def dudx(x,y):\n",
    "    return 2*x\n",
    "\n",
    "def dudy(x,y):\n",
    "    return 2*y\n",
    "\n",
    "def dvdx(x,y):\n",
    "    return 2*x\n",
    "\n",
    "def dvdy(x,y):\n",
    "    return -2*y\n",
    "\n",
    "def u(x,y):\n",
    "    return x**2 + y**2 - 10\n",
    "\n",
    "def v(x,y):\n",
    "    return x**2 - y**2 - 1\n",
    "\n",
    "J = [[dudx,dudy],[dvdx,dvdy]]\n",
    "F = [[u],[v]]\n",
    "B = [[1],[1]]\n",
    "E = 0.01\n",
    "\n",
    "for i in range(100):\n",
    "    Ji = createMatrix(2,2,0)\n",
    "    Jin,Jim = getDimensions(Ji)\n",
    "    for k in range(Jin):\n",
    "        for j in range(Jim):\n",
    "            Ji[k][j] = J[k][j](B[0][0],B[1][0])\n",
    "    print(Ji)\n",
    "    Jinv = getMatrizInversa(Ji)\n",
    "    print(Jinv)\n",
    "    Fi = createMatrix(2,1,0)\n",
    "    for k in range(2):\n",
    "        Fi[k][0] = F[k][0](B[0][0],B[1][0])\n",
    "    Bi = restaMatrix(B,multMatrix(Jinv,Fi))\n",
    "    Be = restaMatrix(B,Bi)\n",
    "    if abs(Be[0][0]) < E and abs(Be[1][0]):\n",
    "        B = Bi\n",
    "        break\n",
    "    B = Bi\n",
    "\n",
    "print(\"La solucion es\",B)\n",
    "print(\"u\",u(B[0][0],B[1][0]))\n",
    "print(\"v\",v(B[0][0],B[1][0]))"
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