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
`maximum independent vertex set problem <http://mathworld.wolfram.com/MaximumIndependentVertexSet.html>`__.
The tetrahedra belonging to the maximum independent vertex set are retained for the next Monte Carlo iteration and supplemented by randomly place vertices to produce a new over-packed sample.

LICENSE
-------

MIT. See `License File <https://github.com/maxhutch/packtets/blob/master/LICENSE>`__.

.. |Build Status| image:: https://travis-ci.org/maxhutch/packtets.svg
   :target: https://travis-ci.org/maxhutch/packtets
.. _
