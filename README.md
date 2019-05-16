# 编译 proto 文件
python -m grpc_tools.protoc --python_out=. --grpc_python_out=. -I. ./proto/test.proto

python -m grpc_tools.protoc: python 下的 protoc 编译器通过 python 模块(module) 实现, 所以说这一步非常省心
--python_out=. :  protobuf 相关的代码的路径, 这里生成到当前目录
--grpc_python_out=. : 编译生成处理 grpc 相关的代码的路径, 这里生成到当前目录
-I. ./proto/test.proto : proto 文件的路径
