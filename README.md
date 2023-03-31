# PyNKDV: An Efficient Network Kernel Density Visualization Library for Geospatial Analytic Systems

Network kernel density visualization (NKDV) has been widely used in different applications, including traffic/traffic accident hotspot detection and crime hotspot detection. Therefore, many software packages, e.g., spNetwork (an R package) and SANET (a plugin for QGIS/ArcGIS), can also support this tool. However, all these software packages are based on the naïve implementation, which are not scalable to large-scale datasets. To overcome this weakness, we propose this python library, called PyNKDV, which is based on our state-of-the-art solution (ADA). PyNKDV can significantly improve the efficiency for generating NKDV compared with existing software packages.