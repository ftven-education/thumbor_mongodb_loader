#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
from tornado.concurrent import return_future
from pymongo import MongoClient
from bson.objectid import ObjectId
import gridfs
from thumbor.loaders import LoaderResult

def __conn__(self):
  the_database = self.config.MONGO_ORIGIN_SERVER_DB
  uri = 'mongodb://'+ self.config.MONGO_ORIGIN_SERVER_HOST
  client = MongoClient(uri)
  #database
  db = client[self.config.MONGO_ORIGIN_SERVER_DB]
  return db

@return_future
def load(self, path, callback):
  db = __conn__(self)
  words2 = path.split("/")
  storage = self.config.MONGO_ORIGIN_SERVER_COLLECTION
  images = gridfs.GridFS(db, collection=storage)
  result = LoaderResult()
  if images.exists(ObjectId(words2[0])):
      contents = images.get(ObjectId(words2[0])).read()
      result.successful = True
      result.buffer = contents
  else:
      result.error = LoaderResult.ERROR_NOT_FOUND
      result.successful = False
  callback(result)