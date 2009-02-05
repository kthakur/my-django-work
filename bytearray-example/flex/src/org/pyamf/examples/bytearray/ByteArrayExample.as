package org.pyamf.examples.bytearray
{
	/**
	 * Copyright (c) 2007-2009 The PyAMF Project.
	 * See LICENSE for details.
	*/

	import flash.media.Camera;
	import flash.media.Video;
	import flash.net.NetConnection;
	import flash.net.Responder;
	
	import flash.events.IOErrorEvent;
	import flash.events.NetStatusEvent;
	
	import mx.collections.ArrayCollection;
	import mx.controls.Button;
	import mx.controls.DataGrid;
	import mx.controls.Image;
	import mx.controls.TextArea;
	import mx.core.Application;
	import mx.core.UIComponent;
	import mx.events.FlexEvent;
	
	/**
	 * This examples shows how to use the ByteArray class in
	 * ActionScript 3. Requires Flex 3 (for JPG encoder).
	 */
	public class ByteArrayExample extends Application
	{
		private var _cam			: Camera;
		private var _snapshotter	: Snapshot;
		private var _gateway		: NetConnection;
		private var _video			: Video;
		private var _width			: int;
		private var _height			: int;
		private var _fps			: int;
		
		public var status_txt		: TextArea;
		public var videoWindow		: UIComponent;
		public var img				: Image;
		public var btn				: Button;
		public var dg				: DataGrid;
		
		[Bindable]
		public var snapshots		: ArrayCollection;
		
		public function ByteArrayExample()
		{
			super();
			addEventListener(FlexEvent.APPLICATION_COMPLETE, onInitApp);
		}
		
		private function onInitApp(event:FlexEvent): void
		{
			// setup video properties
			_width = 320;
			_height = 240;
			_fps = 15;
			
			// setup connection
            _gateway = new NetConnection();
			
            // Connect to gateway (Django needs trailing slash)
            _gateway.connect("http://localhost:8000/");
            
            // addEventListeners for IOErrors and gateway script errors
            _gateway.addEventListener(IOErrorEvent.IO_ERROR, ioErrorHandler);
            _gateway.addEventListener(NetStatusEvent.NET_STATUS, netStatusHandler);
            
            // Set responder property to the object and methods that will receive the 
            // result or fault condition that the service returns.
            var responder:Responder = new Responder( onSnapshotsResult, onFault );
            
            // Call remote service to fetch data
            _gateway.call("getSnapshots", responder);
            
            // Setup snapshot feature
            if ( Camera.names.length == 0 ) 
            {
            	status_txt.text = "No webcams found.\n";
            	btn.enabled = false;
            } 
            else
            {
            	// Enable camera and video
	            _cam = Camera.getCamera();
	            _cam.setMode(_width, _height, _fps);
	            _video = new Video(_width, _height);
	            _video.attachCamera(_cam);
	            videoWindow.width = _width;
				videoWindow.height = _height;
	            videoWindow.addChild(_video);
	            
	            status_txt.text = "Started " + _cam.name + "\n";
            }
		}
		
		public function showPhoto(): void 
		{
			if (dg.selectedItem != null)
			{
				img.load(dg.selectedItem.url);
			}
		}
		
		public function createSnapshot(): void
		{
			// create snapshot
			_snapshotter = new Snapshot(_width, _height);
			_snapshotter.draw(_video);
			
			// save snapshot
			saveSnapshot();
		}
		
		private function saveSnapshot(): void
		{
            // set responder property to the object and methods that will receive the 
            // result or fault condition that the service returns.
            var responder:Responder = new Responder( onSaveResult, onFault );
            
            // call remote service to save jpg wrapped in compressed ByteArray.
            _gateway.call( "ByteArray.saveSnapshot", responder, _snapshotter.jpg );
            
            // wait for result.
            status_txt.text += "Saving snapshot...\n";
            btn.enabled = false;
		}
		
		private function onSnapshotsResult( result:* ): void
        {
        	// add snapshot to list
           	snapshots = result;
           	status_txt.text += "Loaded " + snapshots.length + " snapshot(s).\n";
        }
        
        private function onSaveResult( result:* ): void
        {
            var snapshot:Object = result;
            status_txt.text += "Saved " + snapshot.name + "\n";
            // add url to list
            snapshots.addItemAt(snapshot, 0);
            btn.enabled = true;
        }
        
        private function onFault( error:* ): void
        {
            // notify the user of the problem
            status_txt.text = "Remoting error: \n";
            for ( var d:String in error ) {
               status_txt.text += error[d] + "\n";
            }
            btn.enabled = true;
        }
		
		private function netStatusHandler(event:NetStatusEvent):void
		{
			if (event.info.level == "error")
			{
				// notify the user of the problem
                status_txt.text = "Remoting error: \n";
                for ( var d:String in event.info ) {
                   status_txt.text += event.info[d] + "\n";
                }
                btn.enabled = true;
			}
		}
		
		private function ioErrorHandler(error:IOErrorEvent):void
		{
			// notify the user of the problem
            status_txt.text = "IO error: \n";
            for ( var d:String in error ) {
               status_txt.text += error[d] + "\n";
            }
            btn.enabled = true;
		}
		
	}
}