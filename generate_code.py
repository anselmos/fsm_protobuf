from grpc_tools import protoc

protoc.main((
    '',
    '-I.',
    '--python_out=./fsm_proto/.',
    '--grpc_python_out=./fsm_proto/.',
    'fsm_search.proto',
))
