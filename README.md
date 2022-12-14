<center><h1>P-median problem</h1></center>

The p-median problem is useful to model many real world situations such as the location of public or industrial facilities, warehouses and others. The p-median problem differs from the UFLP in two respects — there are no costs for opening facilities and there is an upper bound on the number of facilities that should be opened. It models the problem of finding a minimum cost clustering and belongs to the class of  NP hard problems in strong sense.

<h2>How to install and run<h2>

1. Copy the git repository
   
   ```console
   foo@bar:~$ git clone https://github.com/cl1ckname/p-median-problem.git
   foo@bar:~$ cd p-median-problem
   ```
2. Install the dependencies
   
   ```console
   foo@bar:~$ pip3 install -r requirements.py
   ```
3. Run the solution using `start.sh`
   
   ```console
   foo@bar:~$ sh start.sh <solution>
   ```

4. If you want to run your own code you need to create a `test.py` in root of project and run
   
   ```console
   foo@bar:~$ sh start.sh test
   ```