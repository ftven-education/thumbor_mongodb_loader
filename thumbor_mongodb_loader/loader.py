#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license

from tornado.concurrent import return_future
from pymongo import MongoClient
from bson.objectid import ObjectId
import gridfs
import urllib


def __conn__(self):
  the_database = self.config.MONGO_ORIGIN_SERVER_DB
  uri = 'mongodb://' + self.config.MONGO_ORIGIN_SERVER_HOST + '/?authSource=' + self.config.MONGO_ORIGIN_SERVER_DB
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

        if images.exists(ObjectId(words2[0])):
            contents = images.get(ObjectId(words2[0])).read()
            callback(contents)
        else:
            callback(None)
