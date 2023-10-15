{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "51cf4499",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "1e61f6cb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "original array\n",
      "[  1   7  13 105]\n",
      "size of the memory occupid  by the said array \n",
      "16 bytes \n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "X= np.array([1,7,13,105])\n",
    "print(\"original array\")\n",
    "print(X)\n",
    "print(\"size of the memory occupid  by the said array \")\n",
    "print(\"%d bytes \"%(X.size * X.itemsize))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "26320065",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "An array of size 10 ones\n",
      "[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]\n",
      "An array of size 10 ones \n",
      "[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]\n",
      "An array of 10 fives\n",
      "[6. 6. 6. 6. 6. 6. 6. 6. 6. 6.]\n",
      "An array with random\n",
      "[6. 6. 6. 6. 6. 6. 6. 6. 6. 6.]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "array =np.zeros(10)\n",
    "print(\"An array of size 10 ones\")\n",
    "print (array)\n",
    "array=np.ones(10)\n",
    "print(\"An array of size 10 ones \")\n",
    "print(array)\n",
    "array=np.ones(10)+5\n",
    "print(\"An array of 10 fives\")\n",
    "print(array)\n",
    "\n",
    "print(\"An array with random\")\n",
    "print(array)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "6d361ed9",
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "module 'numpy' has no attribute 'arrange'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "Cell \u001b[1;32mIn [8], line 2\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mnumpy\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mnp\u001b[39;00m\n\u001b[1;32m----> 2\u001b[0m a\u001b[38;5;241m=\u001b[39mnp\u001b[38;5;241m.\u001b[39marrange(\u001b[38;5;241m10\u001b[39m,\u001b[38;5;241m22\u001b[39m)\u001b[38;5;241m.\u001b[39mreshape((\u001b[38;5;241m3\u001b[39m,\u001b[38;5;241m4\u001b[39m))\n\u001b[0;32m      3\u001b[0m \u001b[38;5;28mprint\u001b[39m(a)\n\u001b[0;32m      4\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mEach element of  the array is : \u001b[39m\u001b[38;5;124m\"\u001b[39m)\n",
      "File \u001b[1;32mc:\\users\\pc\\appdata\\local\\programs\\python\\python39\\lib\\site-packages\\numpy\\__init__.py:311\u001b[0m, in \u001b[0;36m__getattr__\u001b[1;34m(attr)\u001b[0m\n\u001b[0;32m    308\u001b[0m     \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mtesting\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m Tester\n\u001b[0;32m    309\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m Tester\n\u001b[1;32m--> 311\u001b[0m \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mAttributeError\u001b[39;00m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmodule \u001b[39m\u001b[38;5;132;01m{!r}\u001b[39;00m\u001b[38;5;124m has no attribute \u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    312\u001b[0m                      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;132;01m{!r}\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;241m.\u001b[39mformat(\u001b[38;5;18m__name__\u001b[39m, attr))\n",
      "\u001b[1;31mAttributeError\u001b[0m: module 'numpy' has no attribute 'arrange'"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "a=np.arrange(10,22).reshape((3,4))\n",
    "print(a)\n",
    "print(\"Each element of  the array is : \")\n",
    "for x in np.nditer(a):\n",
    "    print(x,end=\" \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3b7bd1b5",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
