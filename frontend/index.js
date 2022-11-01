let container = document.querySelector('#teste')
const getSong = async () => {
  try {
    const song = await axios.get('http://localhost:3000/songs/help', {
      headers: {
        'Content-Type': 'application/json',
      },
    })
    getChord(song.data[0])
  } catch (error) {
    console.log(error)
  }
}

const getChord = async (chord) => {
  try {
    const formattedChord = await axios.get(
      `http://localhost:3000/chords/${chord.artist.slug}/${chord.slug}`,
      {
        headers: {
          'Content-Type': 'application/json',
        },
      }
    )
    //insert the chord into the iframe
    container.innerHTML = formattedChord.data
  } catch (error) {
    console.log(error)
  }
}

// getSong()

const teste = () => {
  fetch('http://localhost:3000/chords/the-beatles/help')
    .then((res) => res.json())
    .then((song) => {
      return song
    })
}

let song = teste()
console.log(song)
