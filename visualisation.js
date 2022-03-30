let slider = {
    start:2003,
    end: 2019,
}

function init() {
    initMap();
}

function generateDataByCountry() {
    dataByCountry = {}

    //populate
    for (interview of ess) {
        let country = interview.Country;
        let year = interview.Year_of_interview;

        if (dataByCountry[country] == undefined) {
            dataByCountry[country] = {};
        }

        if (dataByCountry[country][year] == undefined) {
            dataByCountry[country][year] = {}

            dataByCountry[country][year].total = 0;

            dataByCountry[country][year].interest = 0;
            dataByCountry[country][year].trust = 0;
            dataByCountry[country][year].voted = 0;
            dataByCountry[country][year].leftRight = 0;
            dataByCountry[country][year].immigrants = 0;
            dataByCountry[country][year].unemployment = 0;
            dataByCountry[country][year].children = 0;
            dataByCountry[country][year].age = 0;
        }

        dataByCountry[country][year].total++;

        switch(interview.How_interested_in_politics) {
            case "Very interested":
                dataByCountry[country][year].interest += 100;
            break;

            case "Quite interested":
                dataByCountry[country][year].interest += 66;
            break;

            case "Hardly interested":
                dataByCountry[country][year].interest += 33;
            break;
        }

        switch(interview.Trust_in_countrys_parliament) {
            case "No trust at all":
            case "Refusal":
            case "Don't know":
            case "No answer":
                dataByCountry[country][year].trust += 0;
            break;

            case "Complete trust":
                dataByCountry[country][year].trust += 100;
            break;

            default:
                dataByCountry[country][year].trust += parseInt(interview.Trust_in_countrys_parliament) * 10;
        }

        if (interview.Voted_last_national_election == "Yes") {
            dataByCountry[country][year].voted++;
        }

        switch(interview.Placement_on_left_right_scale) {
            case "Left":
                dataByCountry[country][year].leftRight -= 5;
            break;

            case "Right":
                dataByCountry[country][year].leftRight += 5;
            break

            case "Refusal":
            case "Don't know":
            case "No Answer":
                dataByCountry[country][year].leftRight += 0;
            break;

            default:
                let val = parseInt(interview.Placement_on_left_right_scale);
                dataByCountry[country][year].leftRight += (-5 + val);
        }

        switch(interview.Immigrants_make_country_worse_or_better_place_to_live) {
            case "Better place to live":
                dataByCountry[country][year].immigrants += 5;
            break;

            case "Worse place to live":
                dataByCountry[country][year].immigrants += -5;
            break;

            case "Refusal":
            case "Don't know":
            case "No answer":
                dataByCountry[country][year].immigrants += 0;
            break;

            default:
                let val = parseInt(interview.Immigrants_make_country_worse_or_better_place_to_live);
                dataByCountry[country][year].immigrants += (-5 + val);
        }
        
        if (interview.Any_period_of_unemployment_and_work_seeking_lasted_12_months_or_more == "Yes") {
            dataByCountry[country][year].unemployment += 1;
        }

        if (interview.Ever_had_children_living_in_household == "Yes") {
            dataByCountry[country][year].children  += 1;
        }
        
        let age = parseInt(interview.Age_of_respondent)
        if (age > 0) {
            dataByCountry[country][year].age  += age;
        }
    }

    // console.log(dataByCountry);

    //normalise
    //TODO: make relevant adjustments from: https://www.europeansocialsurvey.org/docs/methodology/ESS_weighting_data_1_1.pdf
    for (country of Object.keys(dataByCountry)) {
        for (year of Object.keys(dataByCountry[country])) {
            let data = dataByCountry[country][year];

            //interest - percentage average
            data.interest /= data.total;

            //trust - percentage average
            data.trust /= data.total

            //voted - percentage voted
            data.voted = (data.voted / data.total) * 100;

            //left right - average scale from -5 (very left) to +5 (very right)
            data.leftRight /= data.total;

            //immmigrant opionion - average scale from -5 (very negative) to +5 (very positive)
            data.immigrants /= data.total;

            //unemployment - percentage unemployed
            data.unemployment = (data.unemployment / data.total) * 100;

            //children - percentage with childeren
            data.children = (data.children / data.total) * 100;

            //age - average age
            data.age /= data.total;

            dataByCountry[country][year] = data;
        }
    }
}