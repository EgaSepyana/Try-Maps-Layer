import { Fragment, useState } from 'react'
import { Map, Source, Layer } from 'react-map-gl'
import 'mapbox-gl/dist/mapbox-gl.css';
import './Map.css'
import fetchHandler from './hooks/FetchHandle';
import { ThreeDots } from 'react-loader-spinner'
import ContentWrapper from './components/ContentWrapper';
// import { fetchDataFromApiLocal } from './util/api';
// import {} from './hooks/FetchHandle'

function App() {

  const { data, loading, error } = fetchHandler('api/v1/mvt/color-province')

  // console.log(error)
  return (
    <>
      <ContentWrapper>
        {error ? <h1>{error}</h1> :
          !loading ? (
            <>
              <div className='tooltip-map'>
                {
                  data?.map((layer) => (
                    <div className='province-name'>
                      <div className='box' style={
                        {
                          backgroundColor: layer.color,
                        }
                      }></div>
                      <span>{layer.province}</span>
                    </div>
                  ))
                }
              </div>
              <Map
                mapboxAccessToken='pk.eyJ1Ijoicm9uaWFydGFzaXRpbmphayIsImEiOiJja2pzZGdkZTkxNnpjMnRwNXY4MmJwdTJuIn0.yy8btAs8q76jGtbiZY628w'
                initialViewState={{
                  longitude: 118.5085,
                  latitude: 0.6467,
                  zoom: 4.33
                }}
                minZoom={4}
                maxZoom={14}
                style={{ width: '100%', height: '100vh' }}
                mapStyle="mapbox://styles/mapbox/light-v10"
              >

                {
                  data?.map((layer, i) => (
                    <Fragment key={i}>
                      <Source
                        id={`${layer.province.toLowerCase().replaceAll(" ", "-")}`}
                        type='vector'
                        tiles={[`http://localhost:8000/api/v1/mvt/get-province/{z}/{x}/{y}/?province=${layer.province}&layer_name=geojsonLayer${i}`]}
                        minzoom={0}
                        maxzoom={14}
                      >
                        <Layer
                          id={`${layer.province.toLowerCase().replaceAll(" ", "-")}-layer`}
                          type='fill'
                          source={`${layer.province.toLowerCase().replaceAll(" ", "-")}`}
                          source-layer={`geojsonLayer${i}`}
                          paint={
                            {
                              'fill-antialias': true,
                              'fill-opacity': 0.7,
                              'fill-color': `${layer.color}`,
                              'fill-outline-color': `${layer.color}`,
                            }
                          }
                        />
                      </Source>
                    </Fragment>
                  ))
                }

              </Map>
            </>
          ) : (
            <ThreeDots
              height="80"
              width="80"
              radius="9"
              color="#142d4f"
              ariaLabel="three-dots-loading"
              wrapperStyle={{
                'height': '100vh',
                'width': '100%',
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center',
              }}
              wrapperClassName="loader-container"
              visible={true}
            />
          )
        }
      </ContentWrapper>
    </>
  )
}

export default App

// import 'mapbox-gl/dist/mapbox-gl.css';
// import React, { useRef, useEffect, useState } from 'react';
// import mapboxgl from 'mapbox-gl';
// import './Map.css';

// mapboxgl.accessToken ='pk.eyJ1IjoidWJlcmRhdGEiLCJhIjoiY2pwY3owbGFxMDVwNTNxcXdwMms2OWtzbiJ9.1PPVl0VLUQgqrosrI2nUhg';

// function App() {

//   const mapContainerRef = useRef(null);

//   const [lng, setLng] = useState(118.5085);
//   const [lat, setLat] = useState(0.6467);
//   const [zoom, setZoom] = useState(4.33);

//   // Initialize map when component mounts
//   useEffect(() => {
//     const map = new mapboxgl.Map({
//       container: mapContainerRef.current,
//       style: 'mapbox://styles/mapbox/light-v10',
//       center: [lng, lat],
//       zoom: zoom,
//       minZoom: 4,
//       maxZoom : 14
//     });

//     map.on('load' , () => {
//         map.addLayer(
//           {
//             'id':'geoms',
//             'type':'fill',
//             'source-layer' : 'shapes',
//             'source': {
//               'type' : 'vector',
//               // 'scheme' : 'tms',
//               'tiles' : [
//                 'http://localhost:8621/api/v1/get-mvt/{z}/{x}/{y}/'
//               ],
//               'minzoom' : 4,
//               'maxzoom' : 14
//             },
//             'paint': {
//               'fill-antialias': true,
//               'fill-opacity': 0.25,
//               'fill-color': 'rgb(200,0,0)',
//               'fill-outline-color': 'rgb(255,255,255)',
//             },
//           }
//         )
//       }
//     )

//     // Add navigation control (the +/- zoom buttons)
//     map.addControl(new mapboxgl.NavigationControl(), 'top-right');

//     map.on('move', () => {
//       setLng(map.getCenter().lng.toFixed(4));
//       setLat(map.getCenter().lat.toFixed(4));
//       setZoom(map.getZoom().toFixed(2));
//     });

//     // Clean up on unmount
//     return () => map.remove();
//   }, []);

//   return (
//     <>
//       <div>
//         <div className='sidebarStyle'>
//           <div>
//             Longitude: {lng} | Latitude: {lat} | Zoom: {zoom}
//           </div>
//         </div>
//         <div className='map-container' ref={mapContainerRef} />
//       </div>
//     </>
//   )
// }

// export default App
