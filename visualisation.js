function init() {
    countries = getCountries(ess);

    let select = document.createElement("select");
    select.name = "country";
    select.id = "select-country";

    for (const country of countries) {
        let option = document.createElement("option");
        option.value = country;
        option.text = country;

        select.appendChild(option);
    }

    let label = document.createElement("label");
    label.innerHTML = "Country: "
    label.htmlFor = select.id;

    select.addEventListener("change", handleChangeCountry);

    document.getElementById("controls").appendChild(label).appendChild(select);
    document.getElementById(select.id).value = selectedCountry;

    partyCounts = getPartyCounts(ess, selectedCountry);
    visualise();
}

function handleChangeCountry() {
    let select = document.getElementById("select-country");

    if (select) {
        selectedCountry = select.value;
        partyCounts = getPartyCounts();
        visualise();
    }
}

function visualise() {
    //remove all existing content
    document.getElementById("visualisation").innerHTML = "";

    const minFont = 6;
    const maxFont = window.innerHeight / (1.7 * Object.keys(partyCounts).length);

    let extent = d3.extent(Object.entries(partyCounts), function([party, count]) {
        return count;
    });

    let scale = d3.scaleLinear()
        .range([minFont, maxFont])
        .domain(extent);

    d3.select("#visualisation")
        .selectAll("p")
        .data(Object.entries(partyCounts))
        .enter()
        .append("p")
        .text(function([party, count]) {
            return party;
        })
        .style("font-size", function([party, count]) {
            return scale(count) + "pt";
        });
}

function getCountries() {
    countries = []

    for(let i = 0; i < ess.length; i++) {
        let interview = ess[i];
        
        let country = interview.Country;

        if (!countries.includes(country)) {
            countries.push(country);
        }
    }

    return countries;
}

function getPartyCounts() {
    partyCounts = {}

    for(let i = 0; i < ess.length; i++) {
        let interview = ess[i];

        let party = interview.Party_voted_for_in_last_national_election;
        let country = interview.Country;
        
        if ((selectedCountry == undefined) || (country == selectedCountry)) {
            if (partyCounts[party] == undefined) {
                partyCounts[party] = 1
            }
            else {
                partyCounts[party] += 1
            }
        }
    }

    //rename not applicable to didn't vote
    Object.defineProperty(partyCounts, "Didn't Vote", Object.getOwnPropertyDescriptor(partyCounts, "Not applicable"));
    delete partyCounts["Not applicable"];

    return partyCounts;
}