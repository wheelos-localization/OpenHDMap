#!/usr/bin/env python

import lib.proto_utils as proto_utils
from modules.map.proto import map_pb2

from matplotlib.lines import Line2D
from matplotlib.patches import Polygon

class Map:
  def __init__(self):
    self.map_pb = map_pb2.Map()
  
  def load(self, map_file_name):
    res = proto_utils.get_pb_from_file(map_file_name, self.map_pb)
    return res is not None
  
  def save(self, map_output_file):
    proto_utils.write_pb_to_text_file(self.map_pb, map_output_file)

  def draw_roads(self, ax, road_ids):
    pass

  def draw_lanes(self, ax, lane_ids):
    for lane in self.map_pb.lane:
      if len(lane_ids) == 0 or lane.id.id in lane_ids:
        self._draw_lane_boundary(lane, ax, "green")
        self._draw_lane_central(lane, ax, "green")
  
  def draw_junctions(self, ax, junction_ids):
    for junction in self.map_pb.junction:
      if len(junction_ids) == 0 or junction.id.id in junction_ids:
        self._draw_polygon_boundary(junction.polygon, ax, "yellow")

  def draw_signals(self, ax):
    pass

  def draw_crosswalks(self, ax):
    for crosswalk in self.map_pb.crosswalk:
      self._draw_polygon_boundary(crosswalk.polygon, ax, "red")

  def draw_stop_signs(self, ax):
    for stop_sign in self.map_pb.stop_sign:
      for stop_line in stop_sign.stop_line:
        for curve in stop_line.segment:
          self._draw_stop_line(curve.line_segment, ax, "yellow")
  
  def draw_yields(self, ax):
    pass
    # for yield_sign in self.map_pb.yield:
    #   for stop_line in yield_sign.stop_line:
    #     for curve in stop_line.segment:
    #       self._draw_stop_line(curve.line_segment, ax, "yellow")

  def draw_clear_areas(self, ax):
    pass

  def draw_overlaps(self, ax):
    pass

  def draw_speed_bumps(self, ax):
    pass

  def draw_parking_spaces(self, ax):
    pass

  def draw_pnc_junctions(self, ax):
    pass


  @staticmethod
  def _draw_lane_boundary(lane, ax, color_val):
    pass
  
  @staticmethod
  def _draw_lane_central(lane, ax, color_val):
    for curve in lane.central_curve.segment:
      if curve.HasField('line_segment'):
        px = []
        py = []
        for p in curve.line_segment.point:
          px.append(float(p.x))
          py.append(float(p.y))
        ax.plot(px, py, ls='-', linewidth=5, c=color_val, alpha=0.5)
  
  @staticmethod
  def _draw_polygon_boundary(polygon, ax, color_val):
    px = []
    py = []
    for point in polygon.point:
      px.append(point.x)
      py.append(point.y)
    ax.plot(px, py, ls='-', linewidth=5, c=color_val, alpha=0.5)

  @staticmethod
  def _draw_polygon(polygon, plt, color_val):
    # todo(zero): need to fix
    pxy = []
    for point in polygon.point:
      pxy.append([point.x,point.y])
    polygon = Polygon(pxy, True)
    fig, ax = plt.subplots()
    ax.add_patch(polygon)

  @staticmethod
  def _draw_stop_line(line_segment, ax, color_val):
    px = []
    py = []
    for p in line_segment.point:
      px.append(float(p.x))
      py.append(float(p.y))
    ax.plot(px, py, 'o-')

