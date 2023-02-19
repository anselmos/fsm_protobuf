from grpc_tools import protoc

protoc.main((
    '',
    '-Iproto',
    '--python_out=./',
    '--grpc_python_out=./',
    'proto/fsm_proto/fsm_search.proto',
))
