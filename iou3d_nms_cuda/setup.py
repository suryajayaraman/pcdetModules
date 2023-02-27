from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension


if __name__ == '__main__':
    setup(
        name='iou3d_nms_cuda',
        ext_modules=[CUDAExtension('iou3d_nms_cuda', 
                [
                    'iou3d_cpu.cpp',
                    'iou3d_nms_api.cpp',
                    'iou3d_nms.cpp',
                    'iou3d_nms_kernel.cu',    
                ])],
        cmdclass={'build_ext': BuildExtension})


    #     name='pcdetModules',
    #     description='Modules commonly used for Lidar Point Cloud based 3D object detection',
    #     cmdclass={
    #         'build_ext': BuildExtension,
    #     },
    #     ext_modules=[
    #         make_cuda_ext(
    #             name='iou3d_nms_cuda',
    #             module='iou3d_nms',
    #             sources=[
                    
    #             ]
    #         ),
    #         make_cuda_ext(
    #             name='roiaware_pool3d_cuda',
    #             module='roiaware_pool3d',
    #             sources=[
    #                 'src/roiaware_pool3d.cpp',
    #                 'src/roiaware_pool3d_kernel.cu',
    #             ]
    #         ),
    #         make_cuda_ext(
    #             name='roipoint_pool3d_cuda',
    #             module='roipoint_pool3d',
    #             sources=[
    #                 'src/roipoint_pool3d.cpp',
    #                 'src/roipoint_pool3d_kernel.cu',
    #             ]
    #         ),
    #         make_cuda_ext(
    #             name='pointnet2_stack_cuda',
    #             module='pointnet2.pointnet2_stack',
    #             sources=[
    #                 'src/pointnet2_api.cpp',
    #                 'src/ball_query.cpp',
    #                 'src/ball_query_gpu.cu',
    #                 'src/group_points.cpp',
    #                 'src/group_points_gpu.cu',
    #                 'src/sampling.cpp',
    #                 'src/sampling_gpu.cu', 
    #                 'src/interpolate.cpp', 
    #                 'src/interpolate_gpu.cu',
    #                 'src/voxel_query.cpp', 
    #                 'src/voxel_query_gpu.cu',
    #                 'src/vector_pool.cpp',
    #                 'src/vector_pool_gpu.cu'
    #             ],
    #         ),
    #         make_cuda_ext(
    #             name='pointnet2_batch_cuda',
    #             module='pointnet2.pointnet2_batch',
    #             sources=[
    #                 'src/pointnet2_api.cpp',
    #                 'src/ball_query.cpp',
    #                 'src/ball_query_gpu.cu',
    #                 'src/group_points.cpp',
    #                 'src/group_points_gpu.cu',
    #                 'src/interpolate.cpp',
    #                 'src/interpolate_gpu.cu',
    #                 'src/sampling.cpp',
    #                 'src/sampling_gpu.cu',

    #             ],
    #         ),
    #     ],
    # )
