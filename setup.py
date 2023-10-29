import os.path as osp
from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

ROOT = osp.dirname(osp.abspath(__file__))

setup(
    name='droid_backends',
    ext_modules=[
        CUDAExtension('droid_backends',
                      include_dirs=[osp.join(ROOT, 'thirdparty/eigen')],
                      sources=[
                          'src/lib/droid.cpp',
                          'src/lib/droid_kernels.cu',
                          'src/lib/correlation_kernels.cu',
                          'src/lib/altcorr_kernel.cu',
                      ],
                      extra_compile_args={
                          'cxx': ['-O3'],
                          'nvcc': ['-O3',
                                   '-gencode=arch=compute_86,code=sm_86',
                                   '-gencode=arch=compute_89,code=sm_89',
                                   ]
                      }),
    ],
    cmdclass={'build_ext': BuildExtension}
)
