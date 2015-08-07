var gulp = require('gulp'),
    minifycss = require('gulp-minify-css'),
    concat = require('gulp-concat'),
    less = require('gulp-less'),
    gulpif = require('gulp-if'),
    order = require('gulp-order'),
    gutil = require('gulp-util'),
    rename = require('gulp-rename'),
    foreach = require('gulp-foreach'),
    debug = require('gulp-debug'),
    path =require('path'),
    merge = require('merge-stream'),
    del = require('del'),
    uglify = require('gulp-uglify');

gulp.task('scripts', function(){
    return gulp.src([
        'bower_components/jquery/dist/jquery.js',
        'bower_components/bootstrap/dist/js/bootstrap.js'
    ])
        .pipe(concat('vendor.js'))
        .pipe(gulp.dest('blog/static/js'))
        .pipe(rename('vendor.min.js'))
        .pipe(uglify())
        .pipe(gulp.dest('blog/static/js'));
});

gulp.task('default', ['js-fef'], function(){});

gulp.task('default', ['clean'], function() {
    gulp.start('fonts', 'styles', 'scripts');
});

gulp.task('clean', function(cb) {
    del(['blog/static/css', 'blog/static/js', 'blog/static/less', 'blog/static/img', 'blog/static/fonts'], cb)
});

gulp.task('fonts', function() {

    var fileList = [
        'bower_components/bootstrap/dist/fonts/*',
        'bower_components/fontawesome/fonts/*'
    ];

    return gulp.src(fileList)
        .pipe(gulp.dest('blog/static/fonts'));
});

gulp.task('styles', function() {

    var baseContent = '@import "bower_components/bootstrap/less/bootstrap.less";@import "bower_components/bootswatch/$theme$/variables.less";@import "bower_components/bootswatch/$theme$/bootswatch.less";@import "bower_components/bootstrap/less/utilities.less";';
    var isBootswatchFile = function(file) {
        var suffix = 'bootswatch.less';
        return file.path.indexOf(suffix, file.path.length - suffix.length) !== -1;
    }

    var isBootstrapFile = function(file) {
        var suffix = 'bootstrap-',
            fileName = path.basename(file.path);

        return fileName.indexOf(suffix) == 0;
    }

    var fileList = [
        'client/less/main.less',
        'bower_components/bootswatch/**/bootswatch.less',
        'bower_components/fontawesome/css/font-awesome.css'
    ];

    return gulp.src(fileList)
        .pipe(gulpif(isBootswatchFile, foreach(function(stream, file) {
            var themeName = path.basename(path.dirname(file.path)),
                content = replaceAll(baseContent, '$theme$', themeName),
                file = string_src('bootstrap-' +  themeName + '.less', content);

            return file;
        })))
        .pipe(less())
        .pipe(gulp.dest('blog/static/css'))
        .pipe(gulpif(isBootstrapFile, foreach(function(stream, file) {
            var fileName = path.basename(file.path),
                themeName = fileName.substring(fileName.indexOf('-') + 1, fileName.indexOf('.'));

            // http://stackoverflow.com/questions/21719833/gulp-how-to-add-src-files-in-the-middle-of-a-pipe
            // https://github.com/gulpjs/gulp/blob/master/docs/recipes/using-multiple-sources-in-one-task.md
            return merge(stream, gulp.src(['blog/static/css/font-awesome.css', 'blog/static/css/main.css']))
                .pipe(concat('style-' + themeName + ".css"))
                .pipe(gulp.dest('blog/static/css'))
                .pipe(rename({suffix: '.min'}))
                .pipe(minifycss())
                .pipe(gulp.dest('blog/static/css'));
        })))
});

// http://stackoverflow.com/questions/1144783/replacing-all-occurrences-of-a-string-in-javascript
function escapeRegExp(string) {
    return string.replace(/([.*+?^=!:${}()|\[\]\/\\])/g, "\\$1");
}

function replaceAll(string, find, replace) {
  return string.replace(new RegExp(escapeRegExp(find), 'g'), replace);
}

function string_src(filename, string) {
  var src = require('stream').Readable({ objectMode: true })
  src._read = function () {
    this.push(new gutil.File({ cwd: "", base: "", path: filename, contents: new Buffer(string) }))
    this.push(null)
  }
  return src
}
