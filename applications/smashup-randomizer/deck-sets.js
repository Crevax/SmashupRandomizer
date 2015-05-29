var deckSets = [
  {name: "Core"},
  {name: "Awesome Level 9000"},
  {name: "The Obligatory Cthulhu Set"},
  {name: "Science Fiction Double Feature"},
  {name: "The Big Geeky Box"},
  {name: "Monster Smash"},
  {name: "Pretty Pretty Smash Up"}
];

var DeckSets = React.createClass({
  render: function() {
    return (
      <div className="deck-set-container">
        <h1>Deck Sets</h1>
        <DeckSetList deckSets={this.props.deckSets} />
      </div>
    );
  }
});

var DeckSetList = React.createClass({
  render: function() {
    var deckSetNodes = this.props.deckSets.map(function (deckSet) {
      return (
        <DeckSet deckSet={deckSet} key={deckSet.name} />
      )
    });

    return (
      <ul className="deck-sets">
        {deckSetNodes}
      </ul>
    );
  }
})

var DeckSet = React.createClass({
  render: function() {
    return (
      <li>{this.props.deckSet.name}</li>
    );
  }
})

React.render(
  <DeckSets deckSets={deckSets} />,
  document.getElementById('content')
);