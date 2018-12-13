
import React, { Component } from 'react';
import {
  ReactiveBase,
  DataSearch,
  SingleRange,
  ResultList

} from '@appbaseio/reactivesearch';
class App extends Component {
  render() {
    return (
      <ReactiveBase
        app="webRecom"
        credentials="oHyDAVIi2:38acfba8-c9f8-443c-8b2b-52ff6e30fddb"
      >
        <DataSearch
          componentId="mainSearch"
          dataField={["KEYWORD", "KEYWORD.search"]}
          queryFormat="and"
          iconPosition="left"
        />

        cd ..

            <ResultList
              componentId="results"
              dataField="content"
              react={{
                "and": ["mainSearch", "KEYWORD"]}}
              pagination={true}
              size={10}
              onData={(res)=>(
                {

                  "title": res.title || " ",
                  "description":
                  "</span><br/><br/><div class='result-author' TITLE='" + res.title + "'>by "  + res.url + "https://google.com/search?q=" + res.url+"</div>",
                  "url": res.url
                }
              )}
              className="result-data"
              innerClass={{
                "resultStats": "result-stats"
              }}
            />


      </ReactiveBase>
    );
  }
}
export default App;