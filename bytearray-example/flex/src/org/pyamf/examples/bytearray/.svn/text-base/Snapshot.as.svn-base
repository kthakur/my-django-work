package org.pyamf.examples.bytearray
{
	/**
	 * Copyright (c) 2007-2009 The PyAMF Project.
	 * See LICENSE for details.
	*/
	
	import flash.display.Bitmap;
	import flash.display.BitmapData;
	import flash.display.IBitmapDrawable;
	import flash.utils.ByteArray;
	
	import mx.graphics.codec.JPEGEncoder;
	import mx.graphics.codec.PNGEncoder;
	
	public class Snapshot
	{
		private var _png		: PNGEncoder;
		private var _jpg		: JPEGEncoder;
		private var _width		: int;
		private var _height 	: int;
		private var _data		: BitmapData;
		private var _bitmap		: Bitmap;
			
		public function Snapshot( width:int=320, height:int=240 )
		{
			_width = width;
			_height = height;
			_data = new BitmapData( _width,  _height, true );
			_bitmap = new Bitmap( _data );
		}
		
		public function draw( source: IBitmapDrawable ): void
		{
			_data.draw( source );
		}
		
		public function get data(): BitmapData
		{
			return _data;
		}
		
		public function get bitmap(): Bitmap
		{
			return _bitmap;
		}
		
		public function get png(): ByteArray
		{
			_png = new PNGEncoder();
			var ba:ByteArray = _png.encode( _data );
			ba.compress();
			return ba;
		}
		
		public function get jpg(): ByteArray
		{
			_jpg = new JPEGEncoder(100);
			var ba:ByteArray = _jpg.encode( _data );
			ba.compress();
			return ba;
		}
		
	}
}