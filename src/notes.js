import {Card} from 'semantic-ui-react'
import React from 'react'

class NotesComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      error: null,
      isLoaded: false,
      items: []
    };
  }


  processResult(result) {
      if (!result) {
          console.log(result);
          return;
      } else {
          var res = []
          result.articles.forEach(function (item, index) {
            res.push({header: item.summary, meta: item.start.date})
          });
          return res.slice(0, 4);
      }
  }

  componentDidMount() {
    fetch("http://127.0.0.1:8000/notes", {"Access-Control-Allow-Origin": "*"})
      .then(res => res.text())
      .then(
        (result) => {
            console.log(result);
          this.setState({
            isLoaded: true,
            items: result
          });
        },
        (error) => {
          this.setState({
            isLoaded: true,
            error: error
          });
        }
      )
  }

  render() {
    const { error, isLoaded, items } = this.state;
    if (error) {
      return <div>Error: {error.message}</div>;
    } else if (!isLoaded) {
      return <div>Loading...</div>;
    } else {
      return (
          <div>{items}</div>
      );
    }
  }
}

export default NotesComponent
