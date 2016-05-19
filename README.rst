packtets
======

|Build Status|

Pack tetrahedra into crystals.

Summary
-------

`Tetrahedron packing <https://en.wikipedia.org/wiki/Tetrahedron_packing>`__ is an open problem, 
with about 14% between the best known lower and upper bounds.
This package uses a Monte Carlo framework to sample possible packings of arbitrary crystals.
Similar efforts have begin with valid packings, which are then evolved and relaxed thermodynamically.
Instead, we begin with highly collisional over-packings and search for the largest valid sub-packing.
The search is performed by recognizing valid packings as 
`indepdent vertex sets <http://mathworld.wolfram.com/IndependentVertexSet.html>`__ of 
the collision graph and solving the 
`maximum independent vertex set <http://mathworld.wolfram.com/MaximumIndependentVertexSet.html>`__ (MIS) problem.
In geometric contexts, this problem is also known as the 
`maximum disjoint set <https://en.wikipedia.org/wiki/Maximum_disjoint_set>`__ (MDS) problem.
The tetrahedra belonging to the maximum independent vertex set are retained for the next Monte Carlo iteration and supplemented by randomly place vertices to produce a new over-packed sample.

Demo
------

The ``demo`` directory contains a jupyter notebook with a widget interface to the core tetrahedra packing routines and simple visualization.
It can be run directly or, optionally, via a docker image.
To build the image, execute::

  docker build -t packtets-demo -f demo/Dockerfile .

from the top-level directory.  Then, to run the docker image::

  docker run -p 8888:8888 packtets-demo

finally, point your browser to ``http://localhost:8888/notebooks/PackTets.ipynb``.

Method
-------

The method is a refinement of an existing packing.
When starting from scratch, the existing packing is simply empty.

1. **Sample**: Add ``N_add`` tets to the packing, generally producing an over-packing
2. **Graph**: Construct a graph representing the over-packing

   * Tets are vertices.
   * Edges connect colliding tets

3. **MIS**: Find a maximum independent vertex set, which is a valid packing

   *  If there is more than one, pick one randomly.
   *  Remove tets that are not in the MIS.

4. **Relax**: Re-arrange the tets to reduce volume or create gaps.

   *  Unimplemented

5. **Resize**: Change the bounding geometry based on the packing.

   *  Unimplemented

6. If **Graph** took more time than **MIS**, incremenet ``N_add``; otherwise, decrement ``N_add``.
7. Repeat

The **Graph** step is performed in the ``geometry`` package with collision detection in python.
The **MIS** step is performed with the ``python-igraph`` library, which binds to C code.
The **Sample**, **Relax**, and **Resize** steps are critical to the performance of the method, and can be passed into the Monte Carlo refinement function as ``sample``, ``relax``, and ``resize``, respectively.

Advantages
^^^^^^^^^^

* Geometry can be prescribed: can solve specific packing problems
* Periodic or finite boundaries (finite unimplemented)
* No tuning parameters, e.g. pseudo-pressure

Disadvantages
^^^^^^^^^^^^^

* Geometry must be perscribed: will not find optimal geometry, just optimal packing
* MIS and MDS are NP-complete, limiting scalability

LICENSE
-------

MIT. See `License File <https://github.com/maxhutch/packtets/blob/master/LICENSE>`__.

.. |Build Status| image:: https://travis-ci.org/maxhutch/packtets.svg
   :target: https://travis-ci.org/maxhutch/packtets
