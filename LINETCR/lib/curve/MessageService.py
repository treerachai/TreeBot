#
# Autogenerated by Thrift Compiler (0.9.3)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
import logging
from ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class Iface:
  def fetchMessageOperations(self, localRevision, lastOpTimestamp, count):
    """
    Parameters:
     - localRevision
     - lastOpTimestamp
     - count
    """
    pass

  def getLastReadMessageIds(self, chatId):
    """
    Parameters:
     - chatId
    """
    pass

  def multiGetLastReadMessageIds(self, chatIds):
    """
    Parameters:
     - chatIds
    """
    pass


class Client(Iface):
  def __init__(self, iprot, oprot=None):
    self._iprot = self._oprot = iprot
    if oprot is not None:
      self._oprot = oprot
    self._seqid = 0

  def fetchMessageOperations(self, localRevision, lastOpTimestamp, count):
    """
    Parameters:
     - localRevision
     - lastOpTimestamp
     - count
    """
    self.send_fetchMessageOperations(localRevision, lastOpTimestamp, count)
    return self.recv_fetchMessageOperations()

  def send_fetchMessageOperations(self, localRevision, lastOpTimestamp, count):
    self._oprot.writeMessageBegin('fetchMessageOperations', TMessageType.CALL, self._seqid)
    args = fetchMessageOperations_args()
    args.localRevision = localRevision
    args.lastOpTimestamp = lastOpTimestamp
    args.count = count
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_fetchMessageOperations(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = fetchMessageOperations_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.e is not None:
      raise result.e
    raise TApplicationException(TApplicationException.MISSING_RESULT, "fetchMessageOperations failed: unknown result")

  def getLastReadMessageIds(self, chatId):
    """
    Parameters:
     - chatId
    """
    self.send_getLastReadMessageIds(chatId)
    return self.recv_getLastReadMessageIds()

  def send_getLastReadMessageIds(self, chatId):
    self._oprot.writeMessageBegin('getLastReadMessageIds', TMessageType.CALL, self._seqid)
    args = getLastReadMessageIds_args()
    args.chatId = chatId
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_getLastReadMessageIds(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = getLastReadMessageIds_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.e is not None:
      raise result.e
    raise TApplicationException(TApplicationException.MISSING_RESULT, "getLastReadMessageIds failed: unknown result")

  def multiGetLastReadMessageIds(self, chatIds):
    """
    Parameters:
     - chatIds
    """
    self.send_multiGetLastReadMessageIds(chatIds)
    return self.recv_multiGetLastReadMessageIds()

  def send_multiGetLastReadMessageIds(self, chatIds):
    self._oprot.writeMessageBegin('multiGetLastReadMessageIds', TMessageType.CALL, self._seqid)
    args = multiGetLastReadMessageIds_args()
    args.chatIds = chatIds
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_multiGetLastReadMessageIds(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = multiGetLastReadMessageIds_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.e is not None:
      raise result.e
    raise TApplicationException(TApplicationException.MISSING_RESULT, "multiGetLastReadMessageIds failed: unknown result")


class Processor(Iface, TProcessor):
  def __init__(self, handler):
    self._handler = handler
    self._processMap = {}
    self._processMap["fetchMessageOperations"] = Processor.process_fetchMessageOperations
    self._processMap["getLastReadMessageIds"] = Processor.process_getLastReadMessageIds
    self._processMap["multiGetLastReadMessageIds"] = Processor.process_multiGetLastReadMessageIds

  def process(self, iprot, oprot):
    (name, type, seqid) = iprot.readMessageBegin()
    if name not in self._processMap:
      iprot.skip(TType.STRUCT)
      iprot.readMessageEnd()
      x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
      oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
      x.write(oprot)
      oprot.writeMessageEnd()
      oprot.trans.flush()
      return
    else:
      self._processMap[name](self, seqid, iprot, oprot)
    return True

  def process_fetchMessageOperations(self, seqid, iprot, oprot):
    args = fetchMessageOperations_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = fetchMessageOperations_result()
    try:
      result.success = self._handler.fetchMessageOperations(args.localRevision, args.lastOpTimestamp, args.count)
      msg_type = TMessageType.REPLY
    except (TTransport.TTransportException, KeyboardInterrupt, SystemExit):
      raise
    except TalkException as e:
      msg_type = TMessageType.REPLY
      result.e = e
    except Exception as ex:
      msg_type = TMessageType.EXCEPTION
      logging.exception(ex)
      result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
    oprot.writeMessageBegin("fetchMessageOperations", msg_type, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_getLastReadMessageIds(self, seqid, iprot, oprot):
    args = getLastReadMessageIds_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = getLastReadMessageIds_result()
    try:
      result.success = self._handler.getLastReadMessageIds(args.chatId)
      msg_type = TMessageType.REPLY
    except (TTransport.TTransportException, KeyboardInterrupt, SystemExit):
      raise
    except TalkException as e:
      msg_type = TMessageType.REPLY
      result.e = e
    except Exception as ex:
      msg_type = TMessageType.EXCEPTION
      logging.exception(ex)
      result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
    oprot.writeMessageBegin("getLastReadMessageIds", msg_type, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_multiGetLastReadMessageIds(self, seqid, iprot, oprot):
    args = multiGetLastReadMessageIds_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = multiGetLastReadMessageIds_result()
    try:
      result.success = self._handler.multiGetLastReadMessageIds(args.chatIds)
      msg_type = TMessageType.REPLY
    except (TTransport.TTransportException, KeyboardInterrupt, SystemExit):
      raise
    except TalkException as e:
      msg_type = TMessageType.REPLY
      result.e = e
    except Exception as ex:
      msg_type = TMessageType.EXCEPTION
      logging.exception(ex)
      result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
    oprot.writeMessageBegin("multiGetLastReadMessageIds", msg_type, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()


# HELPER FUNCTIONS AND STRUCTURES

class fetchMessageOperations_args:
  """
  Attributes:
   - localRevision
   - lastOpTimestamp
   - count
  """

  thrift_spec = (
    None, # 0
    None, # 1
    (2, TType.I64, 'localRevision', None, None, ), # 2
    (3, TType.I64, 'lastOpTimestamp', None, None, ), # 3
    (4, TType.I32, 'count', None, None, ), # 4
  )

  def __init__(self, localRevision=None, lastOpTimestamp=None, count=None,):
    self.localRevision = localRevision
    self.lastOpTimestamp = lastOpTimestamp
    self.count = count

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 2:
        if ftype == TType.I64:
          self.localRevision = iprot.readI64()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I64:
          self.lastOpTimestamp = iprot.readI64()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I32:
          self.count = iprot.readI32()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('fetchMessageOperations_args')
    if self.localRevision is not None:
      oprot.writeFieldBegin('localRevision', TType.I64, 2)
      oprot.writeI64(self.localRevision)
      oprot.writeFieldEnd()
    if self.lastOpTimestamp is not None:
      oprot.writeFieldBegin('lastOpTimestamp', TType.I64, 3)
      oprot.writeI64(self.lastOpTimestamp)
      oprot.writeFieldEnd()
    if self.count is not None:
      oprot.writeFieldBegin('count', TType.I32, 4)
      oprot.writeI32(self.count)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.localRevision)
    value = (value * 31) ^ hash(self.lastOpTimestamp)
    value = (value * 31) ^ hash(self.count)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class fetchMessageOperations_result:
  """
  Attributes:
   - success
   - e
  """

  thrift_spec = (
    (0, TType.STRUCT, 'success', (MessageOperations, MessageOperations.thrift_spec), None, ), # 0
    (1, TType.STRUCT, 'e', (TalkException, TalkException.thrift_spec), None, ), # 1
  )

  def __init__(self, success=None, e=None,):
    self.success = success
    self.e = e

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.STRUCT:
          self.success = MessageOperations()
          self.success.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 1:
        if ftype == TType.STRUCT:
          self.e = TalkException()
          self.e.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('fetchMessageOperations_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRUCT, 0)
      self.success.write(oprot)
      oprot.writeFieldEnd()
    if self.e is not None:
      oprot.writeFieldBegin('e', TType.STRUCT, 1)
      self.e.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.success)
    value = (value * 31) ^ hash(self.e)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class getLastReadMessageIds_args:
  """
  Attributes:
   - chatId
  """

  thrift_spec = (
    None, # 0
    None, # 1
    (2, TType.STRING, 'chatId', None, None, ), # 2
  )

  def __init__(self, chatId=None,):
    self.chatId = chatId

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 2:
        if ftype == TType.STRING:
          self.chatId = iprot.readString()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('getLastReadMessageIds_args')
    if self.chatId is not None:
      oprot.writeFieldBegin('chatId', TType.STRING, 2)
      oprot.writeString(self.chatId)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.chatId)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class getLastReadMessageIds_result:
  """
  Attributes:
   - success
   - e
  """

  thrift_spec = (
    (0, TType.STRUCT, 'success', (LastReadMessageIds, LastReadMessageIds.thrift_spec), None, ), # 0
    (1, TType.STRUCT, 'e', (TalkException, TalkException.thrift_spec), None, ), # 1
  )

  def __init__(self, success=None, e=None,):
    self.success = success
    self.e = e

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.STRUCT:
          self.success = LastReadMessageIds()
          self.success.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 1:
        if ftype == TType.STRUCT:
          self.e = TalkException()
          self.e.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('getLastReadMessageIds_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRUCT, 0)
      self.success.write(oprot)
      oprot.writeFieldEnd()
    if self.e is not None:
      oprot.writeFieldBegin('e', TType.STRUCT, 1)
      self.e.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.success)
    value = (value * 31) ^ hash(self.e)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class multiGetLastReadMessageIds_args:
  """
  Attributes:
   - chatIds
  """

  thrift_spec = (
    None, # 0
    None, # 1
    (2, TType.LIST, 'chatIds', (TType.STRING,None), None, ), # 2
  )

  def __init__(self, chatIds=None,):
    self.chatIds = chatIds

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 2:
        if ftype == TType.LIST:
          self.chatIds = []
          (_etype666, _size663) = iprot.readListBegin()
          for _i667 in xrange(_size663):
            _elem668 = iprot.readString()
            self.chatIds.append(_elem668)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('multiGetLastReadMessageIds_args')
    if self.chatIds is not None:
      oprot.writeFieldBegin('chatIds', TType.LIST, 2)
      oprot.writeListBegin(TType.STRING, len(self.chatIds))
      for iter669 in self.chatIds:
        oprot.writeString(iter669)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.chatIds)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class multiGetLastReadMessageIds_result:
  """
  Attributes:
   - success
   - e
  """

  thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRUCT,(LastReadMessageIds, LastReadMessageIds.thrift_spec)), None, ), # 0
    (1, TType.STRUCT, 'e', (TalkException, TalkException.thrift_spec), None, ), # 1
  )

  def __init__(self, success=None, e=None,):
    self.success = success
    self.e = e

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.LIST:
          self.success = []
          (_etype673, _size670) = iprot.readListBegin()
          for _i674 in xrange(_size670):
            _elem675 = LastReadMessageIds()
            _elem675.read(iprot)
            self.success.append(_elem675)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 1:
        if ftype == TType.STRUCT:
          self.e = TalkException()
          self.e.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('multiGetLastReadMessageIds_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.LIST, 0)
      oprot.writeListBegin(TType.STRUCT, len(self.success))
      for iter676 in self.success:
        iter676.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.e is not None:
      oprot.writeFieldBegin('e', TType.STRUCT, 1)
      self.e.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.success)
    value = (value * 31) ^ hash(self.e)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
