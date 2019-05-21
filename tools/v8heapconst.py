# Copyright 2019 the V8 project authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can
# be found in the LICENSE file.

# This file is automatically generated by mkgrokdump and should not
# be modified manually.

# List of known V8 instance types.
INSTANCE_TYPES = {
  0: "INTERNALIZED_STRING_TYPE",
  2: "EXTERNAL_INTERNALIZED_STRING_TYPE",
  8: "ONE_BYTE_INTERNALIZED_STRING_TYPE",
  10: "EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE",
  18: "UNCACHED_EXTERNAL_INTERNALIZED_STRING_TYPE",
  26: "UNCACHED_EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE",
  32: "STRING_TYPE",
  33: "CONS_STRING_TYPE",
  34: "EXTERNAL_STRING_TYPE",
  35: "SLICED_STRING_TYPE",
  37: "THIN_STRING_TYPE",
  40: "ONE_BYTE_STRING_TYPE",
  41: "CONS_ONE_BYTE_STRING_TYPE",
  42: "EXTERNAL_ONE_BYTE_STRING_TYPE",
  43: "SLICED_ONE_BYTE_STRING_TYPE",
  45: "THIN_ONE_BYTE_STRING_TYPE",
  50: "UNCACHED_EXTERNAL_STRING_TYPE",
  58: "UNCACHED_EXTERNAL_ONE_BYTE_STRING_TYPE",
  64: "SYMBOL_TYPE",
  65: "HEAP_NUMBER_TYPE",
  66: "BIGINT_TYPE",
  67: "ODDBALL_TYPE",
  68: "MAP_TYPE",
  69: "CODE_TYPE",
  70: "MUTABLE_HEAP_NUMBER_TYPE",
  71: "FOREIGN_TYPE",
  72: "BYTE_ARRAY_TYPE",
  73: "BYTECODE_ARRAY_TYPE",
  74: "FREE_SPACE_TYPE",
  75: "FIXED_INT8_ARRAY_TYPE",
  76: "FIXED_UINT8_ARRAY_TYPE",
  77: "FIXED_INT16_ARRAY_TYPE",
  78: "FIXED_UINT16_ARRAY_TYPE",
  79: "FIXED_INT32_ARRAY_TYPE",
  80: "FIXED_UINT32_ARRAY_TYPE",
  81: "FIXED_FLOAT32_ARRAY_TYPE",
  82: "FIXED_FLOAT64_ARRAY_TYPE",
  83: "FIXED_UINT8_CLAMPED_ARRAY_TYPE",
  84: "FIXED_BIGINT64_ARRAY_TYPE",
  85: "FIXED_BIGUINT64_ARRAY_TYPE",
  86: "FIXED_DOUBLE_ARRAY_TYPE",
  87: "FEEDBACK_METADATA_TYPE",
  88: "FILLER_TYPE",
  89: "ACCESS_CHECK_INFO_TYPE",
  90: "ACCESSOR_INFO_TYPE",
  91: "ACCESSOR_PAIR_TYPE",
  92: "ALIASED_ARGUMENTS_ENTRY_TYPE",
  93: "ALLOCATION_MEMENTO_TYPE",
  94: "ASM_WASM_DATA_TYPE",
  95: "ASYNC_GENERATOR_REQUEST_TYPE",
  96: "CLASS_POSITIONS_TYPE",
  97: "DEBUG_INFO_TYPE",
  98: "ENUM_CACHE_TYPE",
  99: "FUNCTION_TEMPLATE_INFO_TYPE",
  100: "FUNCTION_TEMPLATE_RARE_DATA_TYPE",
  101: "INTERCEPTOR_INFO_TYPE",
  102: "INTERPRETER_DATA_TYPE",
  103: "MODULE_INFO_ENTRY_TYPE",
  104: "MODULE_TYPE",
  105: "OBJECT_TEMPLATE_INFO_TYPE",
  106: "PROMISE_CAPABILITY_TYPE",
  107: "PROMISE_REACTION_TYPE",
  108: "PROTOTYPE_INFO_TYPE",
  109: "SCRIPT_TYPE",
  110: "SOURCE_POSITION_TABLE_WITH_FRAME_CACHE_TYPE",
  111: "STACK_FRAME_INFO_TYPE",
  112: "STACK_TRACE_FRAME_TYPE",
  113: "TEMPLATE_OBJECT_DESCRIPTION_TYPE",
  114: "TUPLE2_TYPE",
  115: "TUPLE3_TYPE",
  116: "ARRAY_BOILERPLATE_DESCRIPTION_TYPE",
  117: "WASM_CAPI_FUNCTION_DATA_TYPE",
  118: "WASM_DEBUG_INFO_TYPE",
  119: "WASM_EXCEPTION_TAG_TYPE",
  120: "WASM_EXPORTED_FUNCTION_DATA_TYPE",
  121: "CALLABLE_TASK_TYPE",
  122: "CALLBACK_TASK_TYPE",
  123: "PROMISE_FULFILL_REACTION_JOB_TASK_TYPE",
  124: "PROMISE_REJECT_REACTION_JOB_TASK_TYPE",
  125: "PROMISE_RESOLVE_THENABLE_JOB_TASK_TYPE",
  126: "FINALIZATION_GROUP_CLEANUP_JOB_TASK_TYPE",
  127: "ALLOCATION_SITE_TYPE",
  128: "EMBEDDER_DATA_ARRAY_TYPE",
  129: "FIXED_ARRAY_TYPE",
  130: "OBJECT_BOILERPLATE_DESCRIPTION_TYPE",
  131: "CLOSURE_FEEDBACK_CELL_ARRAY_TYPE",
  132: "HASH_TABLE_TYPE",
  133: "ORDERED_HASH_MAP_TYPE",
  134: "ORDERED_HASH_SET_TYPE",
  135: "ORDERED_NAME_DICTIONARY_TYPE",
  136: "NAME_DICTIONARY_TYPE",
  137: "GLOBAL_DICTIONARY_TYPE",
  138: "NUMBER_DICTIONARY_TYPE",
  139: "SIMPLE_NUMBER_DICTIONARY_TYPE",
  140: "STRING_TABLE_TYPE",
  141: "EPHEMERON_HASH_TABLE_TYPE",
  142: "SCOPE_INFO_TYPE",
  143: "SCRIPT_CONTEXT_TABLE_TYPE",
  144: "AWAIT_CONTEXT_TYPE",
  145: "BLOCK_CONTEXT_TYPE",
  146: "CATCH_CONTEXT_TYPE",
  147: "DEBUG_EVALUATE_CONTEXT_TYPE",
  148: "EVAL_CONTEXT_TYPE",
  149: "FUNCTION_CONTEXT_TYPE",
  150: "MODULE_CONTEXT_TYPE",
  151: "NATIVE_CONTEXT_TYPE",
  152: "SCRIPT_CONTEXT_TYPE",
  153: "WITH_CONTEXT_TYPE",
  154: "WEAK_FIXED_ARRAY_TYPE",
  155: "TRANSITION_ARRAY_TYPE",
  156: "CALL_HANDLER_INFO_TYPE",
  157: "CELL_TYPE",
  158: "CODE_DATA_CONTAINER_TYPE",
  159: "DESCRIPTOR_ARRAY_TYPE",
  160: "FEEDBACK_CELL_TYPE",
  161: "FEEDBACK_VECTOR_TYPE",
  162: "LOAD_HANDLER_TYPE",
  163: "PREPARSE_DATA_TYPE",
  164: "PROPERTY_ARRAY_TYPE",
  165: "PROPERTY_CELL_TYPE",
  166: "SHARED_FUNCTION_INFO_TYPE",
  167: "SMALL_ORDERED_HASH_MAP_TYPE",
  168: "SMALL_ORDERED_HASH_SET_TYPE",
  169: "SMALL_ORDERED_NAME_DICTIONARY_TYPE",
  170: "STORE_HANDLER_TYPE",
  171: "UNCOMPILED_DATA_WITHOUT_PREPARSE_DATA_TYPE",
  172: "UNCOMPILED_DATA_WITH_PREPARSE_DATA_TYPE",
  173: "WEAK_ARRAY_LIST_TYPE",
  174: "WEAK_CELL_TYPE",
  1024: "JS_PROXY_TYPE",
  1025: "JS_GLOBAL_OBJECT_TYPE",
  1026: "JS_GLOBAL_PROXY_TYPE",
  1027: "JS_MODULE_NAMESPACE_TYPE",
  1040: "JS_SPECIAL_API_OBJECT_TYPE",
  1041: "JS_VALUE_TYPE",
  1056: "JS_API_OBJECT_TYPE",
  1057: "JS_OBJECT_TYPE",
  1058: "JS_ARGUMENTS_TYPE",
  1059: "JS_ARRAY_BUFFER_TYPE",
  1060: "JS_ARRAY_ITERATOR_TYPE",
  1061: "JS_ARRAY_TYPE",
  1062: "JS_ASYNC_FROM_SYNC_ITERATOR_TYPE",
  1063: "JS_ASYNC_FUNCTION_OBJECT_TYPE",
  1064: "JS_ASYNC_GENERATOR_OBJECT_TYPE",
  1065: "JS_CONTEXT_EXTENSION_OBJECT_TYPE",
  1066: "JS_DATE_TYPE",
  1067: "JS_ERROR_TYPE",
  1068: "JS_GENERATOR_OBJECT_TYPE",
  1069: "JS_MAP_TYPE",
  1070: "JS_MAP_KEY_ITERATOR_TYPE",
  1071: "JS_MAP_KEY_VALUE_ITERATOR_TYPE",
  1072: "JS_MAP_VALUE_ITERATOR_TYPE",
  1073: "JS_MESSAGE_OBJECT_TYPE",
  1074: "JS_PROMISE_TYPE",
  1075: "JS_REGEXP_TYPE",
  1076: "JS_REGEXP_STRING_ITERATOR_TYPE",
  1077: "JS_SET_TYPE",
  1078: "JS_SET_KEY_VALUE_ITERATOR_TYPE",
  1079: "JS_SET_VALUE_ITERATOR_TYPE",
  1080: "JS_STRING_ITERATOR_TYPE",
  1081: "JS_WEAK_REF_TYPE",
  1082: "JS_FINALIZATION_GROUP_CLEANUP_ITERATOR_TYPE",
  1083: "JS_FINALIZATION_GROUP_TYPE",
  1084: "JS_WEAK_MAP_TYPE",
  1085: "JS_WEAK_SET_TYPE",
  1086: "JS_TYPED_ARRAY_TYPE",
  1087: "JS_DATA_VIEW_TYPE",
  1088: "JS_INTL_V8_BREAK_ITERATOR_TYPE",
  1089: "JS_INTL_COLLATOR_TYPE",
  1090: "JS_INTL_DATE_TIME_FORMAT_TYPE",
  1091: "JS_INTL_LIST_FORMAT_TYPE",
  1092: "JS_INTL_LOCALE_TYPE",
  1093: "JS_INTL_NUMBER_FORMAT_TYPE",
  1094: "JS_INTL_PLURAL_RULES_TYPE",
  1095: "JS_INTL_RELATIVE_TIME_FORMAT_TYPE",
  1096: "JS_INTL_SEGMENT_ITERATOR_TYPE",
  1097: "JS_INTL_SEGMENTER_TYPE",
  1098: "WASM_EXCEPTION_TYPE",
  1099: "WASM_GLOBAL_TYPE",
  1100: "WASM_INSTANCE_TYPE",
  1101: "WASM_MEMORY_TYPE",
  1102: "WASM_MODULE_TYPE",
  1103: "WASM_TABLE_TYPE",
  1104: "JS_BOUND_FUNCTION_TYPE",
  1105: "JS_FUNCTION_TYPE",
}

# List of known V8 maps.
KNOWN_MAPS = {
  ("read_only_space", 0x00139): (74, "FreeSpaceMap"),
  ("read_only_space", 0x00161): (68, "MetaMap"),
  ("read_only_space", 0x001a5): (67, "NullMap"),
  ("read_only_space", 0x001dd): (159, "DescriptorArrayMap"),
  ("read_only_space", 0x0020d): (154, "WeakFixedArrayMap"),
  ("read_only_space", 0x00235): (88, "OnePointerFillerMap"),
  ("read_only_space", 0x0025d): (88, "TwoPointerFillerMap"),
  ("read_only_space", 0x002a1): (67, "UninitializedMap"),
  ("read_only_space", 0x002e5): (8, "OneByteInternalizedStringMap"),
  ("read_only_space", 0x00341): (67, "UndefinedMap"),
  ("read_only_space", 0x00375): (65, "HeapNumberMap"),
  ("read_only_space", 0x003b9): (67, "TheHoleMap"),
  ("read_only_space", 0x00419): (67, "BooleanMap"),
  ("read_only_space", 0x004a1): (72, "ByteArrayMap"),
  ("read_only_space", 0x004c9): (129, "FixedArrayMap"),
  ("read_only_space", 0x004f1): (129, "FixedCOWArrayMap"),
  ("read_only_space", 0x00519): (132, "HashTableMap"),
  ("read_only_space", 0x00541): (64, "SymbolMap"),
  ("read_only_space", 0x00569): (40, "OneByteStringMap"),
  ("read_only_space", 0x00591): (142, "ScopeInfoMap"),
  ("read_only_space", 0x005b9): (166, "SharedFunctionInfoMap"),
  ("read_only_space", 0x005e1): (69, "CodeMap"),
  ("read_only_space", 0x00609): (149, "FunctionContextMap"),
  ("read_only_space", 0x00631): (157, "CellMap"),
  ("read_only_space", 0x00659): (165, "GlobalPropertyCellMap"),
  ("read_only_space", 0x00681): (71, "ForeignMap"),
  ("read_only_space", 0x006a9): (155, "TransitionArrayMap"),
  ("read_only_space", 0x006d1): (161, "FeedbackVectorMap"),
  ("read_only_space", 0x00725): (67, "ArgumentsMarkerMap"),
  ("read_only_space", 0x00785): (67, "ExceptionMap"),
  ("read_only_space", 0x007e1): (67, "TerminationExceptionMap"),
  ("read_only_space", 0x00849): (67, "OptimizedOutMap"),
  ("read_only_space", 0x008a9): (67, "StaleRegisterMap"),
  ("read_only_space", 0x008ed): (151, "NativeContextMap"),
  ("read_only_space", 0x00915): (150, "ModuleContextMap"),
  ("read_only_space", 0x0093d): (148, "EvalContextMap"),
  ("read_only_space", 0x00965): (152, "ScriptContextMap"),
  ("read_only_space", 0x0098d): (144, "AwaitContextMap"),
  ("read_only_space", 0x009b5): (145, "BlockContextMap"),
  ("read_only_space", 0x009dd): (146, "CatchContextMap"),
  ("read_only_space", 0x00a05): (153, "WithContextMap"),
  ("read_only_space", 0x00a2d): (147, "DebugEvaluateContextMap"),
  ("read_only_space", 0x00a55): (143, "ScriptContextTableMap"),
  ("read_only_space", 0x00a7d): (131, "ClosureFeedbackCellArrayMap"),
  ("read_only_space", 0x00aa5): (87, "FeedbackMetadataArrayMap"),
  ("read_only_space", 0x00acd): (129, "ArrayListMap"),
  ("read_only_space", 0x00af5): (66, "BigIntMap"),
  ("read_only_space", 0x00b1d): (130, "ObjectBoilerplateDescriptionMap"),
  ("read_only_space", 0x00b45): (73, "BytecodeArrayMap"),
  ("read_only_space", 0x00b6d): (158, "CodeDataContainerMap"),
  ("read_only_space", 0x00b95): (86, "FixedDoubleArrayMap"),
  ("read_only_space", 0x00bbd): (137, "GlobalDictionaryMap"),
  ("read_only_space", 0x00be5): (160, "ManyClosuresCellMap"),
  ("read_only_space", 0x00c0d): (129, "ModuleInfoMap"),
  ("read_only_space", 0x00c35): (70, "MutableHeapNumberMap"),
  ("read_only_space", 0x00c5d): (136, "NameDictionaryMap"),
  ("read_only_space", 0x00c85): (160, "NoClosuresCellMap"),
  ("read_only_space", 0x00cad): (138, "NumberDictionaryMap"),
  ("read_only_space", 0x00cd5): (160, "OneClosureCellMap"),
  ("read_only_space", 0x00cfd): (133, "OrderedHashMapMap"),
  ("read_only_space", 0x00d25): (134, "OrderedHashSetMap"),
  ("read_only_space", 0x00d4d): (135, "OrderedNameDictionaryMap"),
  ("read_only_space", 0x00d75): (163, "PreparseDataMap"),
  ("read_only_space", 0x00d9d): (164, "PropertyArrayMap"),
  ("read_only_space", 0x00dc5): (156, "SideEffectCallHandlerInfoMap"),
  ("read_only_space", 0x00ded): (156, "SideEffectFreeCallHandlerInfoMap"),
  ("read_only_space", 0x00e15): (156, "NextCallSideEffectFreeCallHandlerInfoMap"),
  ("read_only_space", 0x00e3d): (139, "SimpleNumberDictionaryMap"),
  ("read_only_space", 0x00e65): (129, "SloppyArgumentsElementsMap"),
  ("read_only_space", 0x00e8d): (167, "SmallOrderedHashMapMap"),
  ("read_only_space", 0x00eb5): (168, "SmallOrderedHashSetMap"),
  ("read_only_space", 0x00edd): (169, "SmallOrderedNameDictionaryMap"),
  ("read_only_space", 0x00f05): (140, "StringTableMap"),
  ("read_only_space", 0x00f2d): (171, "UncompiledDataWithoutPreparseDataMap"),
  ("read_only_space", 0x00f55): (172, "UncompiledDataWithPreparseDataMap"),
  ("read_only_space", 0x00f7d): (173, "WeakArrayListMap"),
  ("read_only_space", 0x00fa5): (141, "EphemeronHashTableMap"),
  ("read_only_space", 0x00fcd): (128, "EmbedderDataArrayMap"),
  ("read_only_space", 0x00ff5): (174, "WeakCellMap"),
  ("read_only_space", 0x0101d): (58, "NativeSourceStringMap"),
  ("read_only_space", 0x01045): (32, "StringMap"),
  ("read_only_space", 0x0106d): (41, "ConsOneByteStringMap"),
  ("read_only_space", 0x01095): (33, "ConsStringMap"),
  ("read_only_space", 0x010bd): (45, "ThinOneByteStringMap"),
  ("read_only_space", 0x010e5): (37, "ThinStringMap"),
  ("read_only_space", 0x0110d): (35, "SlicedStringMap"),
  ("read_only_space", 0x01135): (43, "SlicedOneByteStringMap"),
  ("read_only_space", 0x0115d): (34, "ExternalStringMap"),
  ("read_only_space", 0x01185): (42, "ExternalOneByteStringMap"),
  ("read_only_space", 0x011ad): (50, "UncachedExternalStringMap"),
  ("read_only_space", 0x011d5): (0, "InternalizedStringMap"),
  ("read_only_space", 0x011fd): (2, "ExternalInternalizedStringMap"),
  ("read_only_space", 0x01225): (10, "ExternalOneByteInternalizedStringMap"),
  ("read_only_space", 0x0124d): (18, "UncachedExternalInternalizedStringMap"),
  ("read_only_space", 0x01275): (26, "UncachedExternalOneByteInternalizedStringMap"),
  ("read_only_space", 0x0129d): (58, "UncachedExternalOneByteStringMap"),
  ("read_only_space", 0x012c5): (76, "FixedUint8ArrayMap"),
  ("read_only_space", 0x012ed): (75, "FixedInt8ArrayMap"),
  ("read_only_space", 0x01315): (78, "FixedUint16ArrayMap"),
  ("read_only_space", 0x0133d): (77, "FixedInt16ArrayMap"),
  ("read_only_space", 0x01365): (80, "FixedUint32ArrayMap"),
  ("read_only_space", 0x0138d): (79, "FixedInt32ArrayMap"),
  ("read_only_space", 0x013b5): (81, "FixedFloat32ArrayMap"),
  ("read_only_space", 0x013dd): (82, "FixedFloat64ArrayMap"),
  ("read_only_space", 0x01405): (83, "FixedUint8ClampedArrayMap"),
  ("read_only_space", 0x0142d): (85, "FixedBigUint64ArrayMap"),
  ("read_only_space", 0x01455): (84, "FixedBigInt64ArrayMap"),
  ("read_only_space", 0x0147d): (67, "SelfReferenceMarkerMap"),
  ("read_only_space", 0x014b1): (98, "EnumCacheMap"),
  ("read_only_space", 0x01501): (116, "ArrayBoilerplateDescriptionMap"),
  ("read_only_space", 0x016d9): (101, "InterceptorInfoMap"),
  ("read_only_space", 0x035f5): (89, "AccessCheckInfoMap"),
  ("read_only_space", 0x0361d): (90, "AccessorInfoMap"),
  ("read_only_space", 0x03645): (91, "AccessorPairMap"),
  ("read_only_space", 0x0366d): (92, "AliasedArgumentsEntryMap"),
  ("read_only_space", 0x03695): (93, "AllocationMementoMap"),
  ("read_only_space", 0x036bd): (94, "AsmWasmDataMap"),
  ("read_only_space", 0x036e5): (95, "AsyncGeneratorRequestMap"),
  ("read_only_space", 0x0370d): (96, "ClassPositionsMap"),
  ("read_only_space", 0x03735): (97, "DebugInfoMap"),
  ("read_only_space", 0x0375d): (99, "FunctionTemplateInfoMap"),
  ("read_only_space", 0x03785): (100, "FunctionTemplateRareDataMap"),
  ("read_only_space", 0x037ad): (102, "InterpreterDataMap"),
  ("read_only_space", 0x037d5): (103, "ModuleInfoEntryMap"),
  ("read_only_space", 0x037fd): (104, "ModuleMap"),
  ("read_only_space", 0x03825): (105, "ObjectTemplateInfoMap"),
  ("read_only_space", 0x0384d): (106, "PromiseCapabilityMap"),
  ("read_only_space", 0x03875): (107, "PromiseReactionMap"),
  ("read_only_space", 0x0389d): (108, "PrototypeInfoMap"),
  ("read_only_space", 0x038c5): (109, "ScriptMap"),
  ("read_only_space", 0x038ed): (110, "SourcePositionTableWithFrameCacheMap"),
  ("read_only_space", 0x03915): (111, "StackFrameInfoMap"),
  ("read_only_space", 0x0393d): (112, "StackTraceFrameMap"),
  ("read_only_space", 0x03965): (113, "TemplateObjectDescriptionMap"),
  ("read_only_space", 0x0398d): (114, "Tuple2Map"),
  ("read_only_space", 0x039b5): (115, "Tuple3Map"),
  ("read_only_space", 0x039dd): (117, "WasmCapiFunctionDataMap"),
  ("read_only_space", 0x03a05): (118, "WasmDebugInfoMap"),
  ("read_only_space", 0x03a2d): (119, "WasmExceptionTagMap"),
  ("read_only_space", 0x03a55): (120, "WasmExportedFunctionDataMap"),
  ("read_only_space", 0x03a7d): (121, "CallableTaskMap"),
  ("read_only_space", 0x03aa5): (122, "CallbackTaskMap"),
  ("read_only_space", 0x03acd): (123, "PromiseFulfillReactionJobTaskMap"),
  ("read_only_space", 0x03af5): (124, "PromiseRejectReactionJobTaskMap"),
  ("read_only_space", 0x03b1d): (125, "PromiseResolveThenableJobTaskMap"),
  ("read_only_space", 0x03b45): (126, "FinalizationGroupCleanupJobTaskMap"),
  ("read_only_space", 0x03b6d): (127, "AllocationSiteWithWeakNextMap"),
  ("read_only_space", 0x03b95): (127, "AllocationSiteWithoutWeakNextMap"),
  ("read_only_space", 0x03bbd): (162, "LoadHandler1Map"),
  ("read_only_space", 0x03be5): (162, "LoadHandler2Map"),
  ("read_only_space", 0x03c0d): (162, "LoadHandler3Map"),
  ("read_only_space", 0x03c35): (170, "StoreHandler0Map"),
  ("read_only_space", 0x03c5d): (170, "StoreHandler1Map"),
  ("read_only_space", 0x03c85): (170, "StoreHandler2Map"),
  ("read_only_space", 0x03cad): (170, "StoreHandler3Map"),
  ("map_space", 0x00139): (1057, "ExternalMap"),
  ("map_space", 0x00161): (1073, "JSMessageObjectMap"),
}

# List of known V8 objects.
KNOWN_OBJECTS = {
  ("read_only_space", 0x00189): "NullValue",
  ("read_only_space", 0x001cd): "EmptyDescriptorArray",
  ("read_only_space", 0x00205): "EmptyWeakFixedArray",
  ("read_only_space", 0x00285): "UninitializedValue",
  ("read_only_space", 0x00325): "UndefinedValue",
  ("read_only_space", 0x00369): "NanValue",
  ("read_only_space", 0x0039d): "TheHoleValue",
  ("read_only_space", 0x003f1): "HoleNanValue",
  ("read_only_space", 0x003fd): "TrueValue",
  ("read_only_space", 0x00465): "FalseValue",
  ("read_only_space", 0x00495): "empty_string",
  ("read_only_space", 0x006f9): "EmptyScopeInfo",
  ("read_only_space", 0x00701): "EmptyFixedArray",
  ("read_only_space", 0x00709): "ArgumentsMarker",
  ("read_only_space", 0x00769): "Exception",
  ("read_only_space", 0x007c5): "TerminationException",
  ("read_only_space", 0x0082d): "OptimizedOut",
  ("read_only_space", 0x0088d): "StaleRegister",
  ("read_only_space", 0x014a5): "EmptyEnumCache",
  ("read_only_space", 0x014d9): "EmptyPropertyArray",
  ("read_only_space", 0x014e1): "EmptyByteArray",
  ("read_only_space", 0x014e9): "EmptyObjectBoilerplateDescription",
  ("read_only_space", 0x014f5): "EmptyArrayBoilerplateDescription",
  ("read_only_space", 0x01529): "EmptyClosureFeedbackCellArray",
  ("read_only_space", 0x01531): "EmptyFixedUint8Array",
  ("read_only_space", 0x01545): "EmptyFixedInt8Array",
  ("read_only_space", 0x01559): "EmptyFixedUint16Array",
  ("read_only_space", 0x0156d): "EmptyFixedInt16Array",
  ("read_only_space", 0x01581): "EmptyFixedUint32Array",
  ("read_only_space", 0x01595): "EmptyFixedInt32Array",
  ("read_only_space", 0x015a9): "EmptyFixedFloat32Array",
  ("read_only_space", 0x015bd): "EmptyFixedFloat64Array",
  ("read_only_space", 0x015d1): "EmptyFixedUint8ClampedArray",
  ("read_only_space", 0x015e5): "EmptyFixedBigUint64Array",
  ("read_only_space", 0x015f9): "EmptyFixedBigInt64Array",
  ("read_only_space", 0x0160d): "EmptySloppyArgumentsElements",
  ("read_only_space", 0x0161d): "EmptySlowElementDictionary",
  ("read_only_space", 0x01641): "EmptyOrderedHashMap",
  ("read_only_space", 0x01655): "EmptyOrderedHashSet",
  ("read_only_space", 0x01669): "EmptyFeedbackMetadata",
  ("read_only_space", 0x01675): "EmptyPropertyCell",
  ("read_only_space", 0x01689): "EmptyPropertyDictionary",
  ("read_only_space", 0x016b1): "NoOpInterceptorInfo",
  ("read_only_space", 0x01701): "EmptyWeakArrayList",
  ("read_only_space", 0x0170d): "InfinityValue",
  ("read_only_space", 0x01719): "MinusZeroValue",
  ("read_only_space", 0x01725): "MinusInfinityValue",
  ("read_only_space", 0x01731): "SelfReferenceMarker",
  ("read_only_space", 0x01771): "OffHeapTrampolineRelocationInfo",
  ("read_only_space", 0x0177d): "TrampolineTrivialCodeDataContainer",
  ("read_only_space", 0x01789): "TrampolinePromiseRejectionCodeDataContainer",
  ("read_only_space", 0x01795): "HashSeed",
  ("old_space", 0x00139): "ArgumentsIteratorAccessor",
  ("old_space", 0x0017d): "ArrayLengthAccessor",
  ("old_space", 0x001c1): "BoundFunctionLengthAccessor",
  ("old_space", 0x00205): "BoundFunctionNameAccessor",
  ("old_space", 0x00249): "ErrorStackAccessor",
  ("old_space", 0x0028d): "FunctionArgumentsAccessor",
  ("old_space", 0x002d1): "FunctionCallerAccessor",
  ("old_space", 0x00315): "FunctionNameAccessor",
  ("old_space", 0x00359): "FunctionLengthAccessor",
  ("old_space", 0x0039d): "FunctionPrototypeAccessor",
  ("old_space", 0x003e1): "StringLengthAccessor",
  ("old_space", 0x00425): "InvalidPrototypeValidityCell",
  ("old_space", 0x0042d): "EmptyScript",
  ("old_space", 0x0046d): "ManyClosuresCell",
  ("old_space", 0x00479): "ArrayConstructorProtector",
  ("old_space", 0x00481): "NoElementsProtector",
  ("old_space", 0x00495): "IsConcatSpreadableProtector",
  ("old_space", 0x0049d): "ArraySpeciesProtector",
  ("old_space", 0x004b1): "TypedArraySpeciesProtector",
  ("old_space", 0x004c5): "RegExpSpeciesProtector",
  ("old_space", 0x004d9): "PromiseSpeciesProtector",
  ("old_space", 0x004ed): "StringLengthProtector",
  ("old_space", 0x004f5): "ArrayIteratorProtector",
  ("old_space", 0x00509): "ArrayBufferDetachingProtector",
  ("old_space", 0x0051d): "PromiseHookProtector",
  ("old_space", 0x00531): "PromiseResolveProtector",
  ("old_space", 0x00539): "MapIteratorProtector",
  ("old_space", 0x0054d): "PromiseThenProtector",
  ("old_space", 0x00561): "SetIteratorProtector",
  ("old_space", 0x00575): "StringIteratorProtector",
  ("old_space", 0x00589): "SingleCharacterStringCache",
  ("old_space", 0x00991): "StringSplitCache",
  ("old_space", 0x00d99): "RegExpMultipleCache",
  ("old_space", 0x011a1): "BuiltinsConstantsTable",
}

# List of known V8 Frame Markers.
FRAME_MARKERS = (
  "ENTRY",
  "CONSTRUCT_ENTRY",
  "EXIT",
  "OPTIMIZED",
  "WASM_COMPILED",
  "WASM_TO_JS",
  "JS_TO_WASM",
  "WASM_INTERPRETER_ENTRY",
  "C_WASM_ENTRY",
  "WASM_COMPILE_LAZY",
  "INTERPRETED",
  "STUB",
  "BUILTIN_CONTINUATION",
  "JAVA_SCRIPT_BUILTIN_CONTINUATION",
  "JAVA_SCRIPT_BUILTIN_CONTINUATION_WITH_CATCH",
  "INTERNAL",
  "CONSTRUCT",
  "ARGUMENTS_ADAPTOR",
  "BUILTIN",
  "BUILTIN_EXIT",
  "NATIVE",
)

# This set of constants is generated from a shipping build.
